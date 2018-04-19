from ..Robot import Robot
import cozmo
from cozmo.util import degrees, distance_mm, speed_mmps

def driveForward(self, distance, speed): #decide on units for this
    self.robot.drive_straight(distance_mm(distance), speed_mmps(speed)).wait_for_completed()

def driveBothWheels(self, leftSpeed, rightSpeed, duration):
    self.robot.drive_wheels(speed_mmps(leftSpeed), speed_mmps(rightSpeed))
    time.sleep(duration)

def driveRightWheel(self, speed, duration):
    self.robot.drive_wheels(0, speed_mmps(speed))
    time.sleep(duration)

def driveLeftWheel(self, speed, duration):
    self.robot.drive_wheels(speed_mmps(speed), 0)
    time.sleep(duration)

# def driveToPosition(self, deltaX, deltaY): # Position relative to current location

# def driveToPositionWithAngle():

# def driveToLocation(): # Absolute location relative to known world

def turn(self, angle): #in degrees
    self.robot.turn_in_place(degrees(angle)).wait_for_completed()

# def stop():

###################################################################
# Functions Exported to Robot                                     #
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



