import cozmo;
import logging;
class Robot:
    robot = -1
    _startOn = -1
    dbg = False
    log = -1


    def __init__(self):
        """
            purpose: Initializes an instance of the robot object.
        """
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



    def debug(self, msg):
        """
            Purpose: If debugging is toggled, prints the message to the sreen
            Parameter: Message to debug
        """
        #Dont always show debbugging messages
        if self.dbg:
            self.log.debug(msg)


    def debugToggle(self):
        """
            Purpose: Turn on and off debugging.
        """
        #if not __debug__:
        self.dbg = not self.dbg
    #    else:
    #        self.log.warning("Cannot turn off debugging when '-o' argument provided")


    def start(self, startOn):
        """
            Purpose: create the cozmo robot and begin executing the function provided
            Parameter: reference to function where execution should begin
            PreConditions: Function must exist, should also take one parameter of type this class
        """
        self._startOn = startOn

        #calls proxy to the the start on function
        #Allows us to hide the actual Cozmo robot
        cozmo.run_program(self._begin)

    def _begin(self, cozmo):
        """
            Purpose: provides a way to store the actual cozmo robot as a member of this class.
            Parameters: cozmo robot object
        """
        #acts as a separator for the other output from cozmo
        print("\n\n\t------STARTING------\n")

        #store the robot
        self.robot = cozmo

        #start the function
        self._startOn(self)

        print("\n\t------  DONE  ------\n\n")
