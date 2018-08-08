from ..Robot import Robot
from ..helpers import *


def getCubeByID(self, id : int):
    """Gets a cube object from the cozmo world using the ID provided.

    Arguments:
        id : An integer representing a cube ID. Can only be 1, 2, or 3.

    Returns:
        A light cube object from the Cozmo library.
    """
    #Check that ID is in range
    if not 1 <= id <= 3:
        #log issue
        self.log.warning("Cube id must be in the range 1 to 3")
        self.log.error("The id provided was %d\n" % id)
        return None

    #return the correct cube
    return self.robot.world.get_light_cube(id)


def setCubeColor(self, id : int, color : tuple):
    """Sets all lights on cube to a specific color.

    Arguments:
        id : An integer representing a cube id.

        color : A tuple representing a rgb color. ex ``(255, 0, 0)``.

    .. code-block:: python

        #sets cube 1 lights to red
        robot.setCubeColor(1, (255, 0, 0))

    """
    #get the cube
    cube = self.getCubeByID(id)

    #verify that the cube exists
    if not cube:
        return

    #generate a light using helper functions
    light = rgbToLight(color)

    #debug action
    self.debug("Setting cube %d color to %s\n" % (id, color))

    #set the lights
    cube.set_lights(light)



def setCubeColorHex(self, id : int, color : str):
    """Sets all lights on cube to a specific color using Hex.

    Arguments:
        id : An integer representing a cube id.

        color : A string that is a hex representation of a color. Use form ``'0xFFF'`` or ``'0xFFFFFF'``

    .. code-block:: python

        #sets cube 1 lights to red
        robot.setCubeColorHex(1, '0xFF000')

    """
    #convert color to RGB
    col = hexToRBG(color)

    #verify that color was valid
    if not col:
        self.log.warning("For colors, your hex string should be in the format '0xFFF' or '0xFFFFFF'")
        self.log.error("The hex provided was '%s'" % color)
        return

    #debug the action
    self.debug("Used %s to generate %s " % (color, col))

    #call set cube color with new color
    self.setCubeColor(id, col)


def setCubeColorRGB(self, id : int, red : int, green : int, blue : int):
    """Sets all lights on cube to a specific color using expanded RGB.

    Arguments:
        id : An integer representing a cube id.

        red : An integer representing the red value of a color. Must be between 0 and 255.

        green : An integer representing the green value of a color. Must be between 0 and 255.

        blue : An integer representing the blue value of a color. Must be between 0 and 255.

    .. code-block:: python

        #sets cube 1 lights to red
        robot.setCubeColorRGB(1, 255, 0, 0)

    """
    #create color tuple
    color = (red, green, blue)

    #call set color
    self.setCubeColor(id, color)



def setCubeColorHSV(self, id : int, h : int, s : float, v : float):
    """Sets all lights on cube to a specific color using HSV.

    Arguments:
        id : An integer representing a cube id.

        h : An integer representing Hue of a color. Must be between 0 and 360.

        s : A float representing the saturation a color. Must be between 0 and 1.

        v : A float representing value, or lightness, of a color. Must be between 0 and 1.

    .. code-block:: python

        #sets cube 1 lights to red
        robot.setCubeColorHSV(1, 0, 1, 1)

    """
    #set cube color, after converting to RGB
    self.setCubeColor(id, hsvToRGB((h,s,v)))


def setCubeCorners(self, id : int, colors : list):
    """Set the each light on a cube individually.

    Arguments:
        id : An integer representing a cube id.

        colors : A list comprised of exactly four rgb tuples

    .. code-block:: python

        #Set cube 1's corners to Red, Green, Blue, and Yellow

        colors = [  (255, 0, 0),    #red
                    (0, 255, 0),    #green
                    (0, 0, 255),    #blue
                    (255, 255, 0)]  #yellow

        robot.setCubeCorners(1, colors)

    """
    #get cube
    cube = self.getCubeByID(id)
    #check that cube does exist
    if not cube:
        return

    #generate an array of the lights
    lights = list(map(rgbToLight, colors))

    #debug the action
    self.debug("Setting cube %d corners to %s" % (id, colors))

    #set the corners *lights is list expansion
    cube.set_light_corners(*lights)



def setCubeCornersHex(self, id : int, hex1 : str, hex2 : str, hex3 : str, hex4 : str):
    #create an array of RGB colors using map
    """Set the each light on a cube individually using hex.

    Arguments:
        id : An integer representing a cube id.

        hex1 : A string that is a hex representation of a color to use for corner 1. Use form ``'0xFFF'`` or ``'0xFFFFFF'``

        hex2 : A string that is a hex representation of a color to use for corner 2. Use form ``'0xFFF'`` or ``'0xFFFFFF'``

        hex3 : A string that is a hex representation of a color to use for corner 3. Use form ``'0xFFF'`` or ``'0xFFFFFF'``

        hex4 : A string that is a hex representation of a color to use for corner 4. Use form ``'0xFFF'`` or ``'0xFFFFFF'``


    .. code-block:: python

        #Set cube 1's corners to Red, Green, Blue, and Yellow

        robot.setCubeCornersHex(1, '0xFF0000', '0x00FF00', '0x0000FF', '0xFFFF00')

    """

    colors = list(map(hexToRBG, [hex1, hex2, hex3, hex4]))

    #call set cube corners
    self.setCubeCorners(id, colors)



def setAllBackpackLights(self, color : tuple):
    """Sets all the lights on Cozmo's back to the specified color.

    Arguments:

        color : A tuple representing a RGB color. ex. ``(255, 0, 0)``

    """
    #Debug the action
    self.debug("Setting backpack lights to %s" % color)

    #Call cozmo function
    self.robot.set_all_backpack_lights(rgbToLight(color))



def setAllBackpackLightsRGB(self, r : int, g : int, b : int):
    """Sets all the lights on Cozmo's back to the specified color using expanded RGB.

    Arguments:

        r : An integer represeting the red value of a color. Must be between 0 and 255.

        g : An integer represeting the green value of a color. Must be between 0 and 255.

        b : An integer represeting the blue value of a color. Must be between 0 and 255.

    """
    #create tuple of RGB then call setAllBackpackLights
    self.setAllBackpackLights((r,g,b))



def setAllBackpackLightsHex(self, color : str):
    """Sets all the lights on Cozmo's back to the specified color using Hex

    Arguments:

        color :  A string that is a hex representation of a color. Use form ``'0xFFF'`` or ``'0xFFFFFF'``

    """
    #create rgb color
    col = hexToRBG(color)

    #check that color was valid
    if not col:
        self.log.warning("For colors, your hex string should be in the format '0xFFF' or '0xFFFFFF'")
        self.log.error("The hex provided was '%s'" % color)
        return

    #debug the color
    self.debug("Used %s to generate %s " % (color, col))

    #set the backpack lights
    self.setBackpackLights(col)



def setAllBackpackLightsHSV(self, h : int, s : float, v : float):
    """Sets all the lights on Cozmo's back to the specified color using HSV.

    Arguments:

        h : An integer representing Hue of a color. Must be between 0 and 360.

        s : A float representing the saturation a color. Must be between 0 and 1.

        v : A float representing value, or lightness, of a color. Must be between 0 and 1.

    """
    #convert to RGB then call set all backpack lights
    self.setAllBackpackLights(hsvToRGB((h,s,v)))



def setBackpackLights(self, colors : list):
    """Set all the lights on Cozmo's back individually.

    .. note::

        The Left and Right lights only support shades of red.

    Arguments:

        colors : A list containing exactly 3 or 5 RGB tuples.
            If the list is of length 3, the indexes pertain to the following lights:
                - 0 : Front
                - 1 : Center
                - 2 : Back
            If the list is of length 5, the indexes pertain to the following lights:
                - 0 : Left
                - 1 : Front
                - 2 : Center
                - 3 : Back
                - 4 : Right

    .. code-block:: python

        #Set the backpack lights to red, green, and blue

        colors = [  (255, 0, 0),    #red
                    (0, 255, 0),    #green
                    (0, 0, 255)]    #blue

        robot.setBackpackLights(colors)
    """
    #if list is not correct length
    if len(colors) not in [3,5]:
        #warn the user
        self.log.warning("Please provide 3 or 5 colors for the backpack")
        self.log.error("Provided %d color(s)" % len(colors))
        return

    #if there are only three colors provided
    if len(colors) is 3:
        #Add OFF lights for the left and right
        off = (0,0,0)
        colors = [off, *colors, off]
        self.debug("Added OFF light for left and right\n")

    #create lights from RGB
    lights = list(map(rgbToLight, colors))

    #debug the action
    self.debug("Setting backpack lights to %s" % colors)

    #set the lights
    self.robot.set_backpack_lights(*lights)




###################################################################
# Functions Exported to CozmoBot                                  #
###################################################################

Robot.setBackpackLights             = setBackpackLights
Robot.getCubeByID                   = getCubeByID

Robot.setCubeCorners                = setCubeCorners
Robot.setCubeCornersHex             = setCubeCornersHex

Robot.setCubeColorHSV               = setCubeColorHSV
Robot.setCubeColorRGB               = setCubeColorRGB
Robot.setCubeColorHex               = setCubeColorHex
Robot.setCubeColor                  = setCubeColor

Robot.setAllBackpackLightsHSV       = setAllBackpackLightsHSV
Robot.setAllBackpackLightsHex       = setAllBackpackLightsHex
Robot.setAllBackpackLightsRGB       = setAllBackpackLightsRGB
Robot.setAllBackpackLights          = setAllBackpackLights
