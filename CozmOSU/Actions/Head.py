from ..Robot import Robot
import cozmo.util
from cozmo.robot import MAX_HEAD_ANGLE, MIN_HEAD_ANGLE


def moveHead(self, degrees : float, speed : int = 10):
    """Moves head to specifed position.

    Arguments:
        degrees: A float representing the angle at which to move to head to.
            - 0 : straight forward.
            - 44.5 : Maximum upward angle.
            - -25 : Minimum downward angle.
        speed: An integer representing the speed to move the head at.
            - 10 (default)
    """
    # Get min and max degrees from library
    min = MIN_HEAD_ANGLE.degrees    #-25
    max = MAX_HEAD_ANGLE.degrees    #44.5

    # If out of range
    if not min <= degrees <= max:
        # Log issue
        self.log.warning("Head degrees should be between %s and %s degrees" %  (str(min), str(max)))
        self.log.error("Degrees provided %s.\n" % str(degrees))
        return

    # Debug the action about to happen
    self.debug("Moving head to %s degrees at speed %s." % (str(degrees), str(speed)))

    # Convert degrees to angle class used by cozmo
    degrees = cozmo.util.Angle(degrees = degrees)

    # Execute head movement action
    self.robot.set_head_angle(degrees, speed).wait_for_completed()
    self.setHeadState(degrees.degrees)
    


def moveHeadRad(self, rads : float, speed : int = 10):
    """Move head to specified position using radians.

    Arguments:
        rads: float between min and max
            - 0 : Straight forward
            - 0.xxxx : Maximum upward angle
            - -0.xxxx : Minimum downward angle
        speed: An integer representing the speed to move the head at.
            - 10 (default)
    """

    #get min and max degrees from library
    min = MIN_HEAD_ANGLE.radians
    max = MAX_HEAD_ANGLE.radians

    #if out of range
    if not min <= rads <= max:
        #log issue
        self.log.warning("Head radians should be between %s and %s." %  (str(min), str(max)))
        self.log.error("Radians provided %s." % str(rads))
        return

    #debug the action about to happen
    self.debug("Moving head to %s radians at speed %s." % (str(rads), str(speed)))

    #convert radians to angle class used by cozmo
    rads = cozmo.util.Angle(radians = rads)

    #Execute head movement action
    self.robot.set_head_angle(rads, speed).wait_for_completed()
    self.setHeadState(rad.degrees)
#Use this as a method for robot


def resetHead(self):
    """Restores the head to a forward position."""

    self.moveHead(0)

###################################################################
# Functions Exported to CozmoBot                                  #
###################################################################

Robot.moveHeadRad                   = moveHeadRad
Robot.moveHead                      = moveHead
Robot.resetHead                     = resetHead

