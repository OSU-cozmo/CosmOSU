import cozmo
import logging
import threading
import asyncio
from time import sleep

class Robot:

    robot = -1
    _startOn = -1
    dbg = False
    log = -1
    fileRecorders = {}
    asyncTasks = []

    # set by self.start(...)
    robot = None    # cozmo.robot.Robot
    _startOn = None # callable
    
    # built on init
    log = None      # logging.logger

    dbg = False

    
    kwargDict = {}
    
    # Array of start events.
    #   start events are dictionaries with the form
    #       {
    #           'function': callable,
    #           'params' : tuple,
    #       }
    #
    #   if tuple has one parameter, add a comma to the end.
    #       ex. (True,)
    startEvts = []
    
    #V ertical location of all lines since last evaluation
    visibleLines = []

    # Iterations of camera handlers since last evaluation
    lineIterations = 0
    
    def __init__(self):
        """Initializes an instance of the CozmOsu.Robot object."""
        
        # !!! REFACTOR THIS -> MOVE GENERATE LOGGER TO HELPERS !!!

        # Adding a logger to the robot class
        #   easier to quicky indicate errors/warnings
        #   specific to the robot
        logger = logging.getLogger('Robot')
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # Logs look like
        #   Robot - ERROR : This is an Error
        formatter = logging.Formatter('%(name)s - %(levelname)s\t: %(message)s')
        # using tab to line up all messages

        ch.setFormatter(formatter)

        logger.addHandler(ch)
        self.log = logger

        # !REFACTOR -> This may not be needed anymore
        self.programAlive = True

    def debug(self, msg : str) -> None:
        """If debugging is on, prints the message to the sreen
        
        .. note::
            
            If debugging is not on, the message will not be shown.
         
        Arguments:
            msg : Message to debug through the logger.

        """

        # Dont always show debbugging messages
        if self.dbg:
            self.log.debug(msg)


    def debugToggle(self) -> None:
        """Turn on and off debugging.
            
            This operates as a basic switch.
            
            - If debugging on, then turn off.
            - If debugging off, then turn on.
        """
        # if not __debug__:
        self.dbg = not self.dbg
    #    else:
    #        self.log.warning("Cannot turn off debugging when '-o' argument provided")

   

    def start(self, startOn) -> None:
        """Create the cozmo robot and begin executing the function provided

            Arguments:
                startOn : A function that serves as an entry point for cozmo.
        """

        self._startOn = startOn

        # calls proxy to the the start on function
        # Allows us to hide the actual Cozmo robot
        cozmo.run_program(self._begin, **self.kwargDict)

    def getRobot(self):
        """Gets the Cozmo.robot

            Purpose : Allows front facing code to still access the Cozmo robot directly

        """
        return self.robot

    async def taskHandler(self):
        """Handles asynchronous tasks

            .. warning::

                This is not front facing, do not call this outside of class.

        """

        # While the front facing thread is active
        while self.userThread.isAlive():

            # Iterate through pending async tasks 
            for x in self.asyncTasks:

                # Add the task to the event loop
                asyncio.ensure_future(x['func'](*x['args']))

                # The task is no longer pending, remove it
                self.asyncTasks.remove(x)

            # wait 1/10th of a second before next iteration
            await asyncio.sleep(0.1)

        # User thread is done, start shutdown
        self.cleanShutdown()

    def cleanShutdown(self):
        """Cleans up threads.

            .. warning::

                This is not front facing, do not call this outside of class.

        """
      

        # Join the thread
        self.userThread.join()
        
        # Might need to add asyncio cleanup


    def _begin(self, cozmo) -> None:
        """Wraps the cozmo librarys run_program, to allow wrapper to work.

            .. warning::

                This is not fron facing, do not call this outside of class.
        """

        # Create user thread
        self.userThread = threading.Thread(target=self._startOn, args=(self,))
      
        # acts as a separator for the other output from cozmo

        print("\n\n\t------STARTING------\n")

        # store the robot
        self.robot = cozmo

        # Execute all post initialization operations before user
        #   can interact with robot
        self.postInit()

        # start the thread        
        self.userThread.start()

        #start all background tasks
        asyncio.ensure_future(self.taskHandler())
        asyncio.get_event_loop().run_until_complete(asyncio.gather(*(asyncio.Task.all_tasks())))
        #once the user thread ends, clean shutdown will be called by task handler.

        #execution will resume here
        print("\n\t------  DONE  ------\n\n")
        
        # Clean up file handlers
        for x in self.fileRecorders:
            if not self.fileRecorders[x].closed:
                self.fileRecorders[x].close()

    def postInit(self) -> None:
        """Execute all setup operations that require the robot to be initialized."""

        #Execute all functions that are in startEvents
        for i in range(len(self.startEvts)):
            
            #*self.startEvts[i]('params') used tuple expansion to fill parameters
            #       ex. f(*(False, True)) -> f(False, True)
            self.startEvts[i]['function'](*self.startEvts[i]['params']) 


    def stayOnCharger(self) -> None:
        """Keep Cozmo on the charger.

            .. warning::

                This disables all movement.

            Useful when only using speech, or camera.
        """
        
        cozmo.robot.Robot.drive_off_charger_on_connect = False

    

