from ..Robot import Robot

"""
Say (message):
    Purpose: Robot will audibly say the message provided
    Parameters: Message as a string
"""
def say(self, msg : str, math : bool = True):
    """Cozmo will audibly say back the message.

    Arguments:

        msg : A string that cozmo will say.

        math : A boolean representing whether the expression contains math or not.
            - True (default) : msg contains math.
            - False : msg does not conatin math.

    .. code-block:: python

        robot.say("Hello World")

    """

    #substitute - for minus and negative
    if math:
        msg = checkNegative(msg)
    #Debug
    self.debug("Robot is saying '%s'" % msg)

    #Execute say text action
    self.robot.say_text(msg).wait_for_completed()

#Use this as a member function for robot
Robot.say = say


def checkNegative(exp : str) -> str:
    s = exp.split()
    final = ""
    first = True
    for i in range(len(s)):
        templ = len(s[i])
        if templ > 1 and s[i][1:].isnumeric() and s[i][0] == '-':
            s[i] = 'negative ' + s[i][1:]
        elif '-' in s[i]:
             s[i] = s[i].replace('-', 'minus')

        if not first:
            s[i] = " " + s[i]
        final = final + s[i]
        first = False
    return final
