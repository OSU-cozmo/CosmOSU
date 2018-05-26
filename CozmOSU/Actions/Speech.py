from ..Robot import Robot


def say(self, msg : str):
    """Cozmo will say the message.

    .. note::

        If you would like to say a math expression, use robot.sayMath(...).

    Arguments:

        msg : A string that cozmo will say.

    .. code-block:: python

        robot.say("Hello World")

    """

    self.debug("Robot is saying '%s'" % msg)

    #Execute say text action
    self.robot.say_text(msg).wait_for_completed()

#Use this as a member function for robot
Robot.say = say

def sayMath(self, msg : str):
    """Cozmo will say the message. Should contain math.

    .. note::

        Use this anytime the output should say 'minus' or 'negative' instead of 'dash'.

    .. warning::

        This will have undefined behavior if the message should say 'dash' and 'minus'/'negative'.

    Arguments:

        msg : A string that cozmo will say, containing math.

    .. code-block:: python

        robot.say("5 - 10 = -5")

    """

    #substitute - for minus and negative
    msg = checkNegative(msg)

    #Debug
    self.debug("Robot is saying '%s'" % msg)

    #Execute say text action
    self.robot.say_text(msg).wait_for_completed()

#Use this as a member function for robot
Robot.sayMath = sayMath

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
