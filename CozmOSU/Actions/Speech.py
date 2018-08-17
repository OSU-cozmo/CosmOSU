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


def sayMath(self, msg : str):
    """Cozmo will say the message. Should contain math.

    .. note::

        Use this anytime the output should say 'minus' or 'negative' instead of 'dash'.

    .. warning::

        This will have undefined behavior if the message should say 'dash' and 'minus'/'negative'.

    Arguments:

        msg : A string that cozmo will say, containing math.

    .. code-block:: python

        robot.sayMath("5 - 10 = -5")

    """

    #substitute - for minus and negative
    msg = checkNegative(msg)

    #Debug
    self.debug("Robot is saying '%s'" % msg)

    #Execute say text action
    self.robot.say_text(msg).wait_for_completed()



###################################################################
# Functions Exported to CozmoBot                                  #
###################################################################

Robot.say                           = say
Robot.sayMath                       = sayMath

def checkNegative(exp : str) -> str:
    """Parses string to convert '-' to negative or minus"""
    
    # Split on whitespace
    s = exp.split() 

    # Make empty final string
    final = ""
    first = True

    #For all the split strings
    for i in range(len(s)):
        
        # If string is in form -XXX convert to negative
        templ = len(s[i])
        if templ > 1 and s[i][1:].isnumeric() and s[i][0] == '-':
            s[i] = 'negative ' + s[i][1:]
        
        # Else convert to minus
        elif '-' in s[i]:
             s[i] = s[i].replace('-', 'minus')

        # If not the first, add a space (no leading whitespace)
        if not first:
            s[i] = " " + s[i]

        # Add temp to final
        final = final + s[i]

        # Add whitespace between the rest
        first = False
        
    return final
