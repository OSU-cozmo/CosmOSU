import CozmOSU
from CozmOSU.helpers import buildGradient
from time import sleep

def main(robot):

    res = 20

    red = (255, 0, 0)
    aqua = (0, 255, 255)
    
    rainbow = buildGradient(res, red, aqua) + buildGradient(res, aqua, red)

    loc = 0

    timeToRun = 30
    elapsed = 0

    while elapsed <= timeToRun:
        robot.setCubeColor(1, rainbow[loc % len(rainbow)])
        robot.setCubeColor(2, rainbow[(loc + 1) % len(rainbow)])
        robot.setCubeColor(3, rainbow[(loc + 2)% len(rainbow)])
        
        loc += 1

        sleep(0.1)
        elapsed += 0.1


robot = CozmOSU.Robot()
robot.start(main)