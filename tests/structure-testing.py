import CozmOSU as Robot

robot = Robot.Robot()

def main(cozmo : Robot.Robot):

    cozmo.say("Hello World")

robot.start(main)
