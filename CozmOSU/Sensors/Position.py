from ..Robot import Robot
import time

def calibrateLevelPitch(self) -> float:
    avg = 0
    avg += self.robot.pose_pitch.degrees
    for x in range(4):
        self.driveForward(10, 100)
        avg += self.robot.pose_pitch.degrees
        self.driveForward(-10, 100)
        self.turn(90)
        
    avg = avg / 5
    self.levelPitch = avg
    self.log.info("Pitch Calibrated")
    self.debug("Level Pitch set to %.3f" % self.levelPitch)
    return avg

def getCurrentPitch(self):
    return round(self.robot.pose_pitch.degrees - self.levelPitch, 3)



Robot.calibrateLevelPitch = calibrateLevelPitch
Robot.getCurrentPitch = getCurrentPitch