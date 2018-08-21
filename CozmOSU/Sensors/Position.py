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
        avg += self.robot.pose_pitch.degrees
        time.sleep(length/samples)

    avg = avg / samples
    self.levelPitch = avg
    self.log.info("Pitch Calibrated")
    self.debug("Level Pitch set to %.2f" % self.levelPitch)

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
    if 'pitch' in self.fileRecorders:
        return
    self.fileRecorders['pitch'] = open(fileName, "w+")


    self.asyncTasks.append({
        'func' : self.pitchRecorder,
        'args' : (deltaTime,)
    })
    
   
async def pitchRecorder(self, deltaTime):
    while self.userThread.isAlive():
        self.fileRecorders['pitch'].write("%.2f\n" % self.getCurrentPitch())
        await asyncio.sleep(deltaTime) 
        


Robot.calibrateLevelPitch = calibrateLevelPitch
Robot.getCurrentPitch = getCurrentPitch
Robot.recordPitch = recordPitch
Robot.pitchRecorder = pitchRecorder