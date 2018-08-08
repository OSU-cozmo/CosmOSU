from ..Robot import Robot
import cozmo
import os
import time 

def enableCamera(self,  viewer : bool = False, color : bool = True) -> None:
    """Turn on the cozmo camera.

        .. note::

            This must be called before robot.start(...).

        Arguments:

            viewer: A boolean value for whether or not to use the viewer window.
                Default : False
        
                .. note::
                    
                    The viewer window shows cozmos view in a tkinter window. Closing this window while cozmo is running is problematic and can freeze. Wait for the program to close on its own. Be mindful of infinite loops when this is enabled.
            
            color: A boolean value for whether or not to use color for the camera.
                Default : True


    """

    #Add the values from the parameter to the kwargDict
    self.kwargDict['use_viewer'] = viewer
    self.kwargDict['force_viewer_on_top'] = viewer

    #Create a call after dict with 
    callafter = {
        "function" : self.cameraInit, 
        "params": (color,)
    }

    #Add the dict
    self.startEvts.append(callafter)
    
    #REFACTOR !!! This should be vestigial
    self.linesInZone = None

#Use this as a method for robot
Robot.enableCamera = enableCamera

def cameraInit(self, color : bool) -> None:
    """Initialize the camera with the provided settings.

    .. note::
        
        This is not front facing code, and should only be called within the class after cozmo has been created.

    """
    self.robot.camera.image_stream_enabled = True
    self.robot.camera.color_image_enabled = color

#Use this as a method for robot
Robot.cameraInit = cameraInit


# REFACTOR !!! range may be vestigial 
def watchForLines(self, range : int = 1) -> None:
    """Start watching for lines.

    .. note::

        Enable the camera if you use this function.

    Arguments:
        range: an int representing a range to watch for.

    """

    #Create a dictionary to call after the robot has been built
    callafter = {
        "function" : self.createLineBinding, 
        "params": (range,)
    }

    #Add the dict to the start events
    self.startEvts.append(callafter)

#Use this as a method for robot
Robot.watchForLines = watchForLines

#REFACTOR !!! range may be vestigial
def createLineBinding(self, range : int = 1) -> None:
    """Creates the event to handle line detection.

    .. note:: 

        This is not front facing code, and should only be caleld within the class after cozmo has been created.

    """


    #Verify that calibrated settings have been imported
    if not self.importSettings():
        self.log.error('No Calibration settings found, please run calibration in local')
        self.log.error('the accuracy of the line detection')
        return 

    #Add the event handler to cozmo
    self.robot.add_event_handler(cozmo.world.EvtNewCameraImage, self.detectLines)

    #Notify the user of settings that were imported
    self.log.info('Setting exposure to : %d' % self.exposure)
    self.log.info('Setting Gain to : %2.1f'% self.gain)

    #Set the exposure on the robots camera
    self.robot.camera.set_manual_exposure(self.exposure, self.gain)

#Use this as a method for robot
Robot.createLineBinding = createLineBinding

def calibrateExposure(self, accuracy: float = 0.8, distance : int = 60, start : int = 1) -> tuple:
    """Calibrates the exposure of the camera to detect lines at a specific distance.

        .. warning:: 
            Currently only works at distance 60mm. Working on variable distance.

        .. note::
            Saves the calibration settings to the current working directory in a file called '.settings.cozmo'. This means that settings will have to be copied or recalibrated for each directory. Working on a system-wide solution.

        .. note::

            This assumes that the robot is already a specific distance from a line, with it in its Field Of View (FOV). The line must also be horizontal, and straight.

        Arguments:
            accuracy: A float which represents a percentage of positive detection frequency that will serve as the threshold for a valid line.
                - 0.8 (default)
            
            distance: An integer representing the distance from the forkift to the line in mm.
                - 60 (default)

            start: An integer representing the start value for the exposure. This must be in the range [1:67]. 
                - 1 (default)

                .. note:: 

                    The exposure is incremented. Lower start values, generally work better.
        Return: 
            A tuple, (lines, exposure, gain):
                - lines: A list of the final lines
                - exposure: An integer representing the final exposure value
                - gain: A float representing the final gain value
                
    """
    
    #Inform user of calibration inizialization
    self.log.info('Initializing')
    self.log.info('If no lines are present in Cozmo\'s FOV at the correct distance, results will be eraneous\n')

    #Allow camera to initizalize
    time.sleep(1)

    self.log.info('Starting to calibrate exposure')

    #Set current exposure
    exp = start

    #General gain values
    gain = [1, 1.5, 2, 2.5, 3]

    #Serves as an indicator to switch between gain & exposure modification
    useExp = False

    #Where to access gain arr
    step = 0

    #current lines
    lines = None

    #clear out the lines that have been seen
    self.areLinesVisible() 

    #while there are valid exposure settings
    while exp < 67:

        #set the expusre to the current settings
        self.robot.camera.set_manual_exposure(exp, gain[step])

        #Allow camera to adjust, and to collect enough samples to avoid
        #   false positives
        time.sleep(1)   #REFACTOR !!! Might be able to reduce this

        #Get the lines that the camera saw.
        lines = self.areLinesVisible()

        #zero out the camera
        count = 0

        #iterate through lines and count the lines in the valid range
        if lines is not None:
            for x in lines:
                if x > 275: #REFACTOR !!! Relate this to distance
                    count = count + 1

        #if valid lines were found enough times to meet or exceed the accuracy threshold,
        #   break
        if count >= (accuracy * self.lineIterations):
            break
        
        #Zero out the iterations
        self.lineIterations = 0

        #Increment exposure if it should be used
        if useExp:
            exp = exp + 1
            useExp = False
        #Otherwise, get the next gain
        else:
            step = step + 1

            #if no more gains after increment, then reset and goto exposure
            if step >= len(gain):
                step = 0
                useExp = True
    
    #LOOP EXITED    

    #Store the valid gain & exposure settings
    self.exposure = exp
    self.gain = gain[step]

    #export settings
    self.exportSettings()

    return  (lines, exp, gain[step]) 

#Use this as a method for robot
Robot.calibrateExposure = calibrateExposure


def calibrateToLine(self, accuracy: float = 0.8, distance: int = 60) -> None:
    """Calibrates to a line that the forklift is resting on.

    .. note:: 

        For best accuracy, make sure that cozmo's forklift is on the ground. Place cozmo on the line, such that the forklift and the line make contact.

    Arguments:
        accuracy: A float which represents a percentage of positive detection frequency that will serve as the threshold for a valid line.
            - 0.8 (default)
            
        distance: An integer representing the distance from the forkift to the line in mm.
            - 60 (default)

    """

    #Set head and lift to 0
    self.moveLift(0)
    self.moveHead(0)

    #drive backwards the correct distance
    self.driveForward(-1 * distance, 50)

    #move the lift upward
    self.moveLift(1)

    #calibrate the exposure
    info = self.calibrateExposure(accuracy, distance)
    self.log.info("found lines %s, with exposure %d, and gain %2.1f" % (info[0], info[1], info[2]))

#Use this as a method for robot
Robot.calibrateToLine = calibrateToLine


def exportSettings(self):
    """Export the settings to a file in the current directory called '.settings.cozmo'.

        .. note::
        
            This is not generally front facing, but can be called if you modify settings, and would like to save them.
    """

    #Check that exposure is valid.
    if self.exposure not in range(0, 68):
        self.log.error("Could not calibrate the exposure, try to verify a line")
        self.log.error("is in cozmo's field of view")

    #open the settings file to write (overwrite)
    file = open('.settings.cozmo', 'w')

    #Store gain and exposure 
    file.write('EXPOSURE:%d\n' % self.exposure)
    file.write('GAIN:%f\n' % self.gain)

    #close the file
    file.close()

Robot.exportSettings = exportSettings

def importSettings(self) -> bool:
    """Import the settings from a file in the current directory called '.settings.cozmo'. This does not apply settings.

        .. note::
        
            This is not generally front facing, but can be called if you would like to import the settings again.
        
        Return: 
            A boolean representing the success of the import.

    """

    if not os.path.isfile('.settings.cozmo'):
        return False
    file = open('.settings.cozmo', 'r')
    for line in file.readlines():
        if 'EXPOSURE' in line:
            self.exposure = int(line.split(':')[1])
        if 'GAIN' in line:
            self.gain = float(line.split(':')[1])

            
    file.close
    return True

Robot.importSettings = importSettings