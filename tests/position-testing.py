import CozmOSU
import time
def main(robot : CozmOSU.Robot) -> None:
    robot.calibrateLevelPitch()

    for x in range(10):
        robot.driveForward(10, 100)
        print(robot.getCurrentPitch())
        time.sleep(1)


robot = CozmOSU.Robot()
robot.start(main)