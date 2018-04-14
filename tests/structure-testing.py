import CozmOSU as Robot

robot = Robot.Robot();
robot.using(["Actions"])
def main(cozmo : Robot.Robot):
    cozmo.test();
    cozmo.say();
robot.start(main);
