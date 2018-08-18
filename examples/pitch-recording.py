import CozmOSU


def main(robot):
    robot.calibrateLevelPitch()

    deltaTime = 0.1
    outFile = "pitch-data.txt"

    robot.recordPitch(outFile, deltaTime)


    robot.turn(360)

robot = CozmOSU.Robot()


robot.start(main)
