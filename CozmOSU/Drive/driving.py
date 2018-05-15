from ..Robot import Robot
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def driveForward(self, distance : float, speed : float):
    """Directs Cozmo to travel forward.

    Arguments:
        distance: How far, in millimeters, Cozmo should travel.
        speed: An integer speed at which to drive. Measured in millimeters per second.
    """
    #Convert parameters into Cozmo classes that represent the units
    realDistance = distance_mm(distance)
    realSpeed = speed_mmps(speed)

    #Log action for debugging
    self.debug("Driving forward %s millimeters at a rate of %s mm/s." % (distance, speed))

    #Execute movement
    self.robot.drive_straight(realDistance, realSpeed).wait_for_completed()

def driveBothWheels(self, left : float, right : float, duration : float):
    """Allows for independently driving both sets of wheels at different speeds.

    Arguments:
        left: Rate in millimeters per second that the left wheels should move.
        right: Rate in millimeters per second that the right wheels should move.
        duration: How long both sets of wheels will be driven
    """
    #Convert speeds into Cozmo unit classes
    leftSpeed  = speed_mmps(left)
    rightSpeed = speed_mmps(right)

    #Log action for debugging
    self.debug("Driving left wheels at %s mm/s and right wheels at %s mm/s for %s seconds." % (left, right, duration))

    #Execute movement
    self.robot.drive_wheels(leftSpeed, rightSpeed)
    time.sleep(duration)

def driveRightWheel(self, speed : float, duration : float):
    """Independely control the right set of wheels.

    Arguments:
        speed: Rate in millimeters per second that the right wheels should move.
        duration: How long both tracks will be driven
    """
    #Convert speed into Cozmo unit classes
    rightSpeed = speed_mmps(speed)

    #Log action for debugging
    self.debug("Driving right wheels at %s mm/s for %s seconds." % (speed, duration))

    #Execute movement
    self.robot.drive_wheels(0, rightSpeed)
    time.sleep(duration)

def driveLeftWheel(self, speed, duration):
    """Independely control the left set of wheels.

    Arguments:
        speed: Rate in millimeters per second that the left wheels should move.
        duration: How long both tracks will be driven
    """
    #Convert speed into Cozmo unit classes
    leftSpeed = speed_mmps(speed)

    #Log action for debugging
    self.debug("Driving left wheels at %s mm/s for %s seconds." % (speed, duration))

    #Execute movement
    self.robot.drive_wheels(leftSpeed, 0)
    time.sleep(duration)

# def driveToPosition(self, deltaX, deltaY): # Position relative to current location

# def driveToPositionWithAngle():

# def driveToLocation(): # Absolute location relative to known world

def turn(self, angle : float): #in degrees
    """Rotate Cozmo an amount from the current position.

    Arguments:
        angle: Angle in degrees that Cozmo should turn.
    """
    #Convert parameter into Cozmo angle unit class
    rotationAngle = degrees(angle)

    #Log action for debugging
    self.debug("Rotating %s degrees." % angle)

    #Execute the turn
    self.robot.turn_in_place(rotationAngle).wait_for_completed()

# def stop():

###################################################################
# Functions Exported to CozmoBot                                  #
###################################################################

Robot.driveForward                  = driveForward
Robot.driveBothWheels               = driveBothWheels
Robot.driveRightWheel               = driveRightWheel
Robot.driveLeftWheel                = driveLeftWheel
# Robot.driveToPosition             = driveToPosition
# Robot.driveToPositionWithAngle    = driveToPositionWithAngle
# Robot.driveToLocation             = driveToLocation
Robot.turn                          = turn
# Robot.stop                        = stop
