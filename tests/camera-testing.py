import CozmOSU
import time


def main(robot : CozmOSU.Robot):
    # robot.resetHead()
    # robot.resetLift()

    robot.moveHead(0)
    robot.moveLift(1)
    while not robot.isLineInZone(4):
        robot.driveForward(15, 50)

r = CozmOSU.Robot()

r.stayOnCharger()
r.watchForLines()
r.enableCamera()
r.start(main)

