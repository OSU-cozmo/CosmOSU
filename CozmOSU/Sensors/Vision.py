from ..Robot import Robot
from typing import Union

def getVisibleCube(self, timeout : int = 1) -> Union[int, None]:
    """Gets a cube in Cozmos field of view (FOV)

    Returns:
        - An int representing the ID of the light cube that was found.
        - If no cube was found, returns None.
    """

    cube = None
    
    try:
        # Scan area for cube
        cube = self.robot.world.wait_for_observed_light_cube(timeout = timeout)
        
        # If a cube as found, set the color to green.
        self.setCubeColor(cube.cube_id, (0,255,0))
    
    except:

        # If no cube was found
        #   Set all cube colors to red
        for x in range (1,4):

            self.setCubeColor(x, (255,0,0))
        return None

    # Return the cube ID
    return cube.cube_id

Robot.getVisibleCube = getVisibleCube