from ..Robot import Robot
from ..helpers import *



def getCubeByID(self, id : int):
    if not 1 <= id <= 3:
        self.log.warning("Cube id must be in the range 1 to 3")
        self.log.error("The id provided was %d\n" % id)
        return None
    return self.robot.world.get_light_cube(id)

Robot.getCubeByID = getCubeByID;

#Use tuple for RGB?? or just 3 parameters for this?
def setCubeColor(self, id : int, color : tuple):
    cube = self.getCubeByID(id)
    if not cube:
        return

    light = rgbToLight(color)

    self.debug("Setting cube %d color to %s\n" % (id, color))
    cube.set_lights(light)

Robot.setCubeColor = setCubeColor

def setCubeColorHex(self, id : int, color : str):
    col = hexToRBG(color)
    if not col:
        self.log.warning("For colors, your hex string should be in the format '0xFFF' or '0xFFFFFF'")
        self.log.error("The hex provided was '%s'" % color)
        return

    self.debug("Used '{0}' to generate {1} ".format(color, col))
    self.setCubeColor(id, col)

Robot.setCubeColorHex = setCubeColorHex

def setCubeColorRGB(self, id : int, red : int, green : int, blue : int):
    color = (red, green, blue);
    self.setCubeColor(id, color)

Robot.setCubeColorRGB = setCubeColorRGB

def setCubeColorHSV(self, id : int, h, s, v):
    self.setCubeColor(id, hsvToRGB((h,s,v)))

Robot.setCubeColorHSV = setCubeColorHSV

def setCubeCorners(self, id : int, colors : list):
    cube = self.getCubeByID(id)
    if not cube:
        return
    lights = list(map(rgbToLight, colors))
    self.debug("Setting cube %d corners to %s" % (id, colors))
    cube.set_light_corners(*lights)

Robot.setCubeCorners = setCubeCorners

def setCubeCornersHex(self, id : int, hex1 : str, hex2 : str, hex3 : str, hex4 : str):
    colors = list(map(hexToRBG, [hex1, hex2, hex3, hex4]))
    self.setCubeCorners(id, colors)

Robot.setCubeCornersHex = setCubeCornersHex

def setAllBackpackLights(self, color : tuple):

    self.debug("Setting backpack lights to %s" % color)
    self.robot.set_all_backpack_lights(rgbToLight(color))

Robot.setAllBackpackLights = setAllBackpackLights

def setAllBackpackLightsRGB(self, r, g, b):
    self.setAllBackpackLights((r,g,b))

Robot.setAllBackpackLightsRGB = setAllBackpackLightsRGB

def setAllBackpackLightsHex(self, color : str):
    col = hexToRBG(color)
    if not col:
        self.log.warning("For colors, your hex string should be in the format '0xFFF' or '0xFFFFFF'")
        self.log.error("The hex provided was '%s'" % color)
        return

    self.debug("Used '{0}' to generate {1} ".format(color, col))
    self.setBackpackLights(col)

Robot.setAllBackpackLightsHex = setAllBackpackLightsHex

def setAllBackpackLightsHSV(self, h, s, v):
    self.setAllBackpackLights(hsvToRGB((h,s,v)));

Robot.setAllBackpackLightsHSV = setAllBackpackLightsHSV

def setBackpackLights(self, colors : list):
    if len(colors) not in [3,5]:
        self.log.warning("Please provide 3 or 5 colors for the backpack")
        self.log.error("Provided %d color(s)" % len(colors))
        return

    if len(colors) is 3:
        off = (0,0,0)
        colors = [off, *colors, off]
        self.debug("Added OFF light for left and right\n")
    lights = list(map(rgbToLight, colors))

    self.debug("Setting backpack lights to %s" % colors)
    self.robot.set_backpack_lights(*lights)

Robot.setBackpackLights = setBackpackLights
