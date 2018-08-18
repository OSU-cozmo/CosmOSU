import CozmOSU

def main(robot):
    robot.say("Hello World")

    #Say The sum of 5 plus 5 is 10
    robot.sayMath("The sum of %d + %d is %d" % (5, 5, 5 + 5))

    # Say 5 minus 10 
    robot.sayMath("%d - %d is %d" % (5, 10, 5 - 10))

robot = CozmOSU.Robot()

robot.start(main)