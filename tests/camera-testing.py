import CozmOSU
import time


def calib(robot):
    robot.calibrateToLine(0.9)

def main(robot : CozmOSU.Robot):
    while True:
        robot.driveForward(10, 20)
        lines = robot.areLinesVisible()
        if lines is not None:
            stop = False
            for line in lines:
                if line > 290:
                    stop = True
                    break
        if stop:
            break

r = CozmOSU.Robot()


r.watchForLines()
r.enableCamera(True, False)

#uncomment to test driving with polling
# r.start(main)

#comment out if testing
r.start(calib)
