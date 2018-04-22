import cozmo;
import math;
#NEEDS TESTING
def rgbToLight(color : tuple):
    c = cozmo.lights.Color(rgb = color)
    return cozmo.lights.Light(on_color = c)

def hexToRBG(color):
    if "0x" in color[:2]:
        color = color[2:]
    if len(color) not in [3,6]:
        return None
    step = len(color) // 3

    red = int(color[:step], 16) % 256
    green = int(color[step:step+step], 16) % 256
    blue = int(color[step+step:], 16) % 256

    return (red, green, blue)

def buildGradient(indexes : int, color1 : tuple, color2 : tuple):
    colors = []
    color1 = rgbToHSV(color1)
    color2 = rgbToHSV(color2)

    dif = abs(color2[0] - color1[0])
    flip = False

    if dif > 180:
        dif = dif / 2
        flip = True

    hStep = dif / indexes
    #cannot change tuples, so cast to list
    temp = list(color1)
    colors.append(color1)

    for x in range(1, indexes-1):
        if flip:
            temp[0] = (temp[0] - hStep) % 360
        else:
            temp[0] = (temp[0] + hStep) % 360
        colors.append(tuple(temp))
        
    colors.append(color2)

    return list(map(hsvToRGB, colors))


def rgbToHSV(color : tuple):
    #referenced http://code.activestate.com/recipes/576919-python-rgb-and-hsv-conversion/

    r = color[0] / 255
    g = color[1] / 255
    b = color[2] / 255

    maxC = max(r, g, b)
    minC = min(r, g, b)

    dF = maxC - minC
    h, s, l = 0, 0, 0

    if max is min:
        h = 0
    elif maxC is r:
        h = (60 * ((g - b) / dF) + 360) % 360
    elif maxC is g:
        h = (60 * ((b - r) / dF) + 120) % 360
    elif maxC is b:
        h = (60 * ((r - g) / dF) + 240) % 360

    if maxC is not 0:
        s = dF / maxC
    v = maxC
    return (h, s, v)


def hsvToRGB(color : tuple):
    #referenced http://code.activestate.com/recipes/576919-python-rgb-and-hsv-conversion/
    h = float(color[0])
    s = float(color[1])
    v = float(color[2])

    h60 = h / 60
    h60Floor = math.floor(h60)
    hi = int(h60Floor) % 6

    f = h60 - h60Floor
    p = v * (1 - s)
    q = v * (1 - f * s)
    t = v * (1 - (1 - f) * s)

    r, g, b = 0, 0, 0

    if hi is 0:
        r, g, b = v, t, p
    elif hi is 1:
        r, g, b = q, v, p
    elif hi is 2:
        r, g, b = p, v, t
    elif hi is 3:
        r, g, b = p, q, v
    elif hi is 4:
        r, g, b = t, p, v
    elif hi is 5:
        r, g, b = v, p, q

    r = int(r * 255)
    g = int(g * 255)
    b = int(b * 255)

    return(r, g, b)
