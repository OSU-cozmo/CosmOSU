from ..Robot import Robot
from typing import Union
def getVisibleCube(self) -> Union[int, None]:
    """Gets a cube in Cozmos field of view (FOV)

    Returns:
        - An int representing the ID of the light cube that was found.
        - If no cube was found, returns None.
    """
    cube = None
    try:
        cube = self.robot.world.wait_for_observed_light_cube(timeout = 1)
        print(cube.cube_id)
        self.setCubeColor(cube.cube_id, (0,255,0))
    except:
        for x in range (1,4):
            self.setCubeColor(x, (255,0,0))
        return None

        
    return cube.cube_id

Robot.getVisibleCube = getVisibleCube