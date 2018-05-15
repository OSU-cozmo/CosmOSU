import CozmOSU
import time


def main(robot : CozmOSU.Robot):
    # robot.resetHead()
    # robot.resetLift()

    robot.moveHead(-25)
    robot.moveLift(1)
    # robot.driveForward(10, 50)
    time.sleep(4)
r = CozmOSU.Robot()

# r.stayOnCharger()
r.watchForLines()
r.debugToggle()
r.enableCamera(True, True)
r.start(main)

