import CozmOSU
import cozmo.util
import random
from cozmo.robot import MAX_HEAD_ANGLE, MIN_HEAD_ANGLE

robot = CozmOSU.Robot()

def speech_tests(robot):
    robot.say("Hello World")
    robot.say("The sum of %d + %d is %d" % (5, 5, 10))



def liftTests(robot):
    robot.moveLift(1.1)
    robot.moveLift(-0.1)

    for x in range(5):
        robot.moveLift((x+1)/5)
    for x in range(5):
        robot.moveLiftSlow((x+1)/5)
    robot.resetLift()

def headTests(robot):

    degs = (int(MIN_HEAD_ANGLE.degrees), int(MAX_HEAD_ANGLE.degrees))
    rads = (MIN_HEAD_ANGLE.radians, MIN_HEAD_ANGLE.radians)

    print("\n\t> STARTING HEAD TESTS\n")
    #should print warning
    robot.moveHead(-50)

    #Should be valid
    robot.moveHead(40)

#    print(">> Full range of motion test\n")
    # *degs is tuple expansion
    for x in range(*degs, 10):
        robot.moveHead(x)

    #Should print warning
    robot.moveHeadRad(20)
    robot.resetHead()


#robot.start(speech_tests);
#robot.start(liftTests);
robot.start(headTests)
