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


    def __init__(self):
        """Initializes an instance of the robot object."""
        #Adding a logger to the robot class
        #easier to quicky indicate errors/warnings
        #specific to the robot
        logger = logging.getLogger('Robot')
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        #Logs look like
        #Robot > ERROR >> This is and Error
        formatter = logging.Formatter('%(name)s > %(levelname)s\t>> %(message)s')
        #using tab to line up all messages

        ch.setFormatter(formatter)

        logger.addHandler(ch)
        self.log = logger

        self.programAlive = True

    def debug(self, msg : str):
        """If debugging is toggled, prints the message to the sreen

        Arguments:
            msg : Message to debug throught the logger.

        *If debugging is not toggled, the message will not be shown*
        """
        #Dont always show debbugging messages
        if self.dbg:
            self.log.debug(msg)


    def debugToggle(self):
        """Turn on and off debugging."""
        #if not __debug__:
        self.dbg = not self.dbg
    #    else:
    #        self.log.warning("Cannot turn off debugging when '-o' argument provided")


    def start(self, startOn):
        """Create the cozmo robot and begin executing the function provided

            Arguments:
                startOn : A reference to function where execution should begin
        """
        self._startOn = startOn

        #calls proxy to the the start on function
        #Allows us to hide the actual Cozmo robot
        cozmo.run_program(self._begin)

    def getRobot(self):
        return self.robot

    async def taskHandler(self):
        while self.userThread.isAlive():
            for x in self.asyncTasks:
                asyncio.ensure_future(x['func'](*x['args']))
                self.asyncTasks.remove(x)
            await asyncio.sleep(0.1)

        self.cleanShutdown()

    def cleanShutdown(self):
        if self.userThread.isAlive():
            self.userThread.join()
        



    def _begin(self, cozmo):
        """
            Purpose: provides a way to store the actual cozmo robot as a member of this class.
            Parameters: cozmo robot object
        """
        self.userThread = threading.Thread(target=self._startOn, args=(self,))
      
        #acts as a separator for the other output from cozmo
        print("\n\n\t------STARTING------\n")

        #store the robot
        self.robot = cozmo

        #start the function
        # self._startOn(self)
        
        self.userThread.start()

        #start all background tasks
        asyncio.ensure_future(self.taskHandler())
        asyncio.get_event_loop().run_until_complete(asyncio.gather(*(asyncio.Task.all_tasks())))
        #once the user thread ends, clean shutdown will be called by task handler.

        #execution will resume here
        print("\n\t------  DONE  ------\n\n")
    

        for x in self.fileRecorders:
            if not self.fileRecorders[x].closed:
                self.fileRecorders[x].close()
