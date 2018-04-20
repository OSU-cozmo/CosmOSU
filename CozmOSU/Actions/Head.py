from ..Robot import Robot
import cozmo.util
from cozmo.robot import MAX_HEAD_ANGLE, MIN_HEAD_ANGLE

"""
Move Head (degrees, speed)
    Purpose: Moves the head to specified angle
    Parameters: degrees -> int or float between -25 and 44.5 degrees
                speed   -> int default(10)
"""
def moveHead(self, degrees, speed = 10):

    #get min and max degrees from library
    min = MIN_HEAD_ANGLE.degrees    #-25
    max = MAX_HEAD_ANGLE.degrees    #44.5

    #if out of range
    if not min <= degrees <= max:
        #log issue
        self.log.warning("Head degrees should be between %s and %s degrees" %  (str(min), str(max)))
        self.log.error("Degrees provided %s.\n" % str(degrees))
        return

    #debug the action about to happen
    self.debug("Moving head to %s degrees at speed %s." % (str(degrees), str(speed)))

    #convert degrees to angle class used by cozmo
    degrees = cozmo.util.Angle(degrees = degrees)

    #Execute head movement action
    self.robot.set_head_angle(degrees, speed).wait_for_completed()

#Use this as a method for robot
Robot.moveHead = moveHead

"""
Move Head Rad (radians, speed)
    Purpose: Moves the head to specified angle
    Parameters: radians -> float between min and max
                speed   -> int default(10)
"""
def moveHeadRad(self, rads, speed = 10):

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
    self.robot.set_head_angle(rads, speed).wait_for_completed();

#Use this as a method for robot
Robot.moveHeadRad = moveHeadRad


"""
Reset Head
    Purpose: Puts head to 0 degrees, straight forward
    PostConditions: Head is looking straight forward
"""
def resetHead(self):
    self.moveHead(0)

#Use this as a method for robot
Robot.resetHead = resetHead
