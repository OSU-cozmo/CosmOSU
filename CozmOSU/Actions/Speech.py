from ..Robot import Robot

"""
Say (message):
    Purpose: Robot will audibly say the message provided
    Parameters: Message as a string
"""
def say(self, msg):

        #Debug
        self.debug("Robot is saying '%s'" % msg)

        #Execute say text action
        self.robot.say_text(msg).wait_for_completed()

#Use this as a member function for robot
Robot.say = say
