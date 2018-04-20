from ..Robot import Robot
from cozmo.robot import MAX_LIFT_HEIGHT, MIN_LIFT_HEIGHT

#To do, add funcitonality for mm and inches


"""
Move Lift (height, speed)
    Purpose: Move lift to a ratio of max height
    Parameters: height -> float between 0 and 1 inclusive
                speed  -> int > 0 (default 25)
"""
def moveLift(self, height, speed = 25):
    #check if in range
    if not 0 <= height <= 1:
        #log issue
        self.log.warning("Lift height should be between 0 and 1.")
        self.log.error("height provided %s.\n" % str(height))
        return

    #debug the action about to happen
    self.debug("Moving lift to height %s at speed %s." % (str(height), str(speed)))
    #Execute actual lift action
    self.robot.set_lift_height(height, speed).wait_for_completed()

#Use this as a method for robot
Robot.moveLift = moveLift

"""
Reset Lift
    Purpose: Puts lift back to the ground
"""
def resetLift(self):
        self.moveLift(0)

#Use this as a method for robot
Robot.resetLift = resetLift
