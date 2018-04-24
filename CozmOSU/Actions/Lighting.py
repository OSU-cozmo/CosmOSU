from ..Robot import Robot
from ..helpers import *


"""
Get Cube By ID (id)
    Purpose : gets a cube object from the cozmo world using the ID
    Parameters : integer between 1 and 3
    Return : Respective light cube
"""
def getCubeByID(self, id : int):
    #Check that ID is in range
    if not 1 <= id <= 3:
        #log issue
        self.log.warning("Cube id must be in the range 1 to 3")
        self.log.error("The id provided was %d\n" % id)
        return None

    #return the correct cube
    return self.robot.world.get_light_cube(id)

#Use this as a method for robot
Robot.getCubeByID = getCubeByID;

"""
Set Cube Color (id, color)

    Purpose : Sets all lights on cube to color provided
    Parameters: ID -> integer, id of the cube
                Color -> tuple in form (r, g, b)
"""
def setCubeColor(self, id : int, color : tuple):
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

#Use this as a method for robot
Robot.setCubeColor = setCubeColor


"""
Set Cube Color Hex (id, color)
    Purpose : sets the color of a cube
    Parameters: ID -> int, id of the cube
                color -> string, in format "0xFFF" or "0xFFFFFF"
"""
def setCubeColorHex(self, id : int, color : str):
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

#Use this as a method for robot
Robot.setCubeColorHex = setCubeColorHex

"""
Set Cube Color RGB
    Purpose : set the color of a cube.
    Parameters: id -> int, id of the cube
                red -> int, 0-255
                green -> int, 0-255
                blue -> int, 0-255
"""
def setCubeColorRGB(self, id : int, red : int, green : int, blue : int):
    #create color tuple
    color = (red, green, blue)

    #call set color
    self.setCubeColor(id, color)

#Use this as a method for robot
Robot.setCubeColorRGB = setCubeColorRGB

"""
Set Cube Color HSV (id, h, s, v)
    Purpose : set color of cube using HSV
    Parameters: ID -> int, cube to use
                h -> int, 0-360
                s -> float, 0-1
                v -> float, 0-1
"""
def setCubeColorHSV(self, id : int, h : int, s : float, v : float):
    #set cube color, after converting to RGB
    self.setCubeColor(id, hsvToRGB((h,s,v)))

#Use this as a method for robot
Robot.setCubeColorHSV = setCubeColorHSV

"""
Set Cube Corners (id, colors)
    Purpose : set the color of individual corner lights
    Parameters: ID -> int, cube to use
                Colors -> list of length 4, where each index
                            is an rgb tupleself.
                            ex [(255,0,0) ... ]
"""
def setCubeCorners(self, id : int, colors : list):
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

#Use this as a method for robot
Robot.setCubeCorners = setCubeCorners

"""
Set Cube Corners Hex (id, hex1, hex2, hex3, hex4)
    Purpose : set the cube corners using a hex values
    Parameters: ID -> int, cube to use
                HexX -> Hex color string in format '0xFFF' or '0xFFFFFF'
"""
def setCubeCornersHex(self, id : int, hex1 : str, hex2 : str, hex3 : str, hex4 : str):
    #create an array of RGB colors using map
    colors = list(map(hexToRBG, [hex1, hex2, hex3, hex4]))

    #call set cube corners
    self.setCubeCorners(id, colors)

#Use this as a method for robot
Robot.setCubeCornersHex = setCubeCornersHex

"""
Set All Backpack Lights (color)
    Purpose : set all the backpack lights on cozmo to one color
    Parameter : Color -> tuple, in form (r, g, b)
"""
def setAllBackpackLights(self, color : tuple):
    #Debug the action
    self.debug("Setting backpack lights to %s" % color)

    #Call cozmo function
    self.robot.set_all_backpack_lights(rgbToLight(color))

#Use this as a method for robot
Robot.setAllBackpackLights = setAllBackpackLights

"""
Set All Backpack Lights RGB (r, g, b)
    Purpose : set all backpack lights to one color
    Parameters: r -> int, red value 0 - 255
                g -> int, green value 0 - 255
                b -> int, blue value 0 - 255
"""
def setAllBackpackLightsRGB(self, r : int, g : int, b : int):
    #create tuple of RGB then call setAllBackpackLights
    self.setAllBackpackLights((r,g,b))

#Use this as a method for robot
Robot.setAllBackpackLightsRGB = setAllBackpackLightsRGB

"""
Set All Backpack Lights Hex (color)
    Purpose : set all backpack lights to one color using hex
    Parameters: color -> str, hex color val in format '0xFFF' or '0xFFFFFF'
"""
def setAllBackpackLightsHex(self, color : str):
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

#Use this as a method for robot
Robot.setAllBackpackLightsHex = setAllBackpackLightsHex

"""
Set All Backpack Lights HSV (h, s, v)
    Purpose : Set all backpack lights to one color usign HSV
    Parameters: h -> int, hue value 0-360
                s -> float, saturation value 0 - 1
                v -> float, value 0 - 1
"""
def setAllBackpackLightsHSV(self, h : int, s : float, v : float):
    #convert to RGB then call set all backpack lights
    self.setAllBackpackLights(hsvToRGB((h,s,v)));

#Use this as a method for robot
Robot.setAllBackpackLightsHSV = setAllBackpackLightsHSV

"""
Set Backpack Lights (colors)
    Purpose : Set each individual light on the backpack.
    Parameters: Colors -> list, length 3 or 5
        index : 0 -> Front          index : 0 -> Left
                1 -> Center                 1 -> Front
                2 -> Back                   2 -> Center
                                            3 -> Back
                                            4 -> Right
    Note : Left and Right lights only support shades of red
"""
def setBackpackLights(self, colors : list):
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

#Use this as a method for robot
Robot.setBackpackLights = setBackpackLights
