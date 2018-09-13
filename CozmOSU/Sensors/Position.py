from ..Robot import Robot
import time
import asyncio

def calibrateLevelPitch(self, length : float = 1.0, samples : int = 20) -> float:
    """Calibrates pitch on a level surface.

    Arguments:
        length: A float representing how many seconds to calibrate for.
            - Default (1.0)
        samples: An integer representing how many samples to take.
            - Default (20)

    Returns:
        - A float representing the calibrated level value in degrees.

    """
    avg = 0

    
    for i in range(samples):
        # Running total of all pitches
        avg += self.robot.pose_pitch.degrees

        # wait
        time.sleep(length/samples)

    # Get average and save
    avg = avg / samples
    self.levelPitch = avg

    # Log info
    self.log.info("Pitch Calibrated")
    self.debug("Level Pitch set to %.2f" % self.levelPitch)

    # Clear the file if it already exits.
    if 'pitch' in self.fileRecorders:
        self.fileRecorders['pitch'].truncate(0)

    return avg

def getCurrentPitch(self) -> float:
    """Gets the current pitch of the Robot.

    Returns:
        - A float representing the current pitch in degrees.

    .. warning::

        You must calibrate the pitch before calling this function.

        .. code-block:: python

            robot.calibrateLevelPitch()
            robot.getCurrentPitch()

    """
    # Get pitch, use calibrated level. Round to 2 decimal places
    return round(self.robot.pose_pitch.degrees - self.levelPitch, 2)

def recordPitch(self, fileName : str = "pitch-data.txt" , deltaTime : float = 0.5) -> None:
    """Records pitch to a file until execution ends.

    Arguments:
        fileName: A string representing the file to save the data to.
            - Default ("pitch-data.txt")
        deltaTime: An float representing how long to wait between each recording.
            - Default (0.5)

    .. warning::

        You must calibrate the pitch before calling this function.

        .. code-block:: python

            robot.calibrateLevelPitch()
            robot.recordPitch("pitch-data.txt", 0.1)

    """

    # Make sure to not duplicate file recorder
    if 'pitch' in self.fileRecorders:
        return
    
    # Create new file
    self.fileRecorders['pitch'] = open(fileName, "w+")

    # Append a task to record
    self.asyncTasks.append({
        'func' : self.pitchRecorder,
        'args' : (deltaTime,)
    })
    
   
async def pitchRecorder(self, deltaTime):
    """Records pitch to a file asynchronously.


    .. warning::

        This is not front facing. Task must be spawned internally.

    """
    
    # Verify that the thread is active
    while self.userThread.isAlive():

        # Write the new pitch to the file
        self.fileRecorders['pitch'].write("%.2f\n" % self.getCurrentPitch())

        # await
        await asyncio.sleep(deltaTime) 
        


Robot.calibrateLevelPitch = calibrateLevelPitch
Robot.getCurrentPitch = getCurrentPitch
Robot.recordPitch = recordPitch
Robot.pitchRecorder = pitchRecorder