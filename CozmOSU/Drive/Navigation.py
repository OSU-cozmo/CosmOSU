from ..Robot import Robot
import cozmo


def pickupCube(self, id : int):
    """Picks up a cube based on ID.

    Arguments:
        id: An int representing the light cube ID.
            - Must be 1, 2, or 3.
        

    .. note::

        Will use 3 retries.

    .. code-block:: python

        robot.pickupCube(2)
    """
    if id not in [1, 2, 3]:
        self.log.warning("Id should be 1, 2, or 3.")
        self.log.error("Id provided was %s.\n" % str(id))
        return
    self.robot.pickup_object(self.getCubeByID(id), num_retries = 3).wait_for_completed()


Robot.pickupCube = pickupCube