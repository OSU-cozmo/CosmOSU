from ..Robot import Robot
from cozmo.robot import MAX_LIFT_HEIGHT, MIN_LIFT_HEIGHT

#To do, add funcitonality for mm and inches


def moveLift(self, height : float, speed : int = 25):
    """Moves lift to a specified height.

    Arguments:
        height : A float representing the height to set the lift to.
            - 0 : On the ground
            - 1 : Maximum height
        speed : An integer representing the speed to move the lift at.
            - 10 (default)
    """
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

def resetLift(self):
    """Puts the lift back to the ground."""
    self.moveLift(0)

#Use this as a method for robot
Robot.resetLift = resetLift
