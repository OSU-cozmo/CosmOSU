from ..Robot import Robot
import cozmo


def pickupCube(self, id : int):
    self.robot.pickup_object(self.getCubeByID(id), num_retries = 3).wait_for_completed()


Robot.pickupCube = pickupCube