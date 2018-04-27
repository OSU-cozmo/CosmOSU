from ..Robot import Robot

"""
Say (message):
    Purpose: Robot will audibly say the message provided
    Parameters: Message as a string
"""
def say(self, msg : str):
    """Cozmo will audibly say back the message.

    Arguments:

        msg : A string that cozmo will say.

    .. code-block:: python

        robot.say("Hello World")

    """

    #Debug
    self.debug("Robot is saying '%s'" % msg)

    #Execute say text action
    self.robot.say_text(msg).wait_for_completed()

#Use this as a member function for robot
Robot.say = say
