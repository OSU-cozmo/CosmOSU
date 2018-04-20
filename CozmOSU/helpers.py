import cozmo;

#NEEDS TESTING
def rgbToLight(color : tuple):
    c = cozmo.lights.Color(rgb = color)
    return cozmo.lights.Light(on_color = c)
