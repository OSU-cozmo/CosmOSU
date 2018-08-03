from ..Robot import Robot
import time
import asyncio
def calibrateLevelPitch(self, length : float = 1.0, samples : int = 20) -> float:
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
    return round(self.robot.pose_pitch.degrees - self.levelPitch, 3)

def recordPitch(self, fileName, deltaTime : float = 0.5) -> None:
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