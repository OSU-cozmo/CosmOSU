import CozmOSU
import cozmo.util
import random
import time
from CozmOSU.helpers import *
from cozmo.robot import MAX_HEAD_ANGLE, MIN_HEAD_ANGLE

robot = CozmOSU.Robot()

def speechTests(robot):
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

    # *degs is tuple expansion
    for x in range(*degs, 10):
        robot.moveHead(x)

    #Should print warning
    robot.moveHeadRad(20)
    robot.resetHead()


def lightTests(robot):

    grad = buildGradient(5, (255,0 ,0), (255,0,255))
    for x in range(1, 4):
        robot.setCubeColor(x, grad[x-1])
    robot.setBackpackLights(grad[:3])
    robot.setCubeCorners(1, grad[:4])
    time.sleep(3)

    #should print error
    robot.setCubeColor(0, (33, 55, 200))
    robot.setCubeColor(4, (33, 55, 200))

    robot.setCubeColorHex(1, '0xFF0000')
    robot.setCubeColorHex(2, '0x00FF00')
    robot.setCubeColorHex(3, '0x0000FF')
    time.sleep(2)

    robot.setCubeColorRGB(1, 0, 255, 0)
    robot.setCubeColorRGB(2, 0, 0, 255)
    robot.setCubeColorRGB(3, 255, 0, 0)
    time.sleep(2)

    cols = [(0, 255, 0), (255, 0, 0), (0, 0, 255), (255, 255, 0)]
    robot.setCubeCorners(1, cols)
    time.sleep(2)

    robot.setCubeCornersHex(1, '0x660FAA', '0xF0F0F0', '0xFF00FF', '0xABCDEF')
    time.sleep(3)

robot.start(lightTests)
#robot.start(speechTests);
#robot.start(liftTests);
#robot.start(headTests)
