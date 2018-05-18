from ..Robot import Robot
import numpy as np
import cv2
import cozmo 

ZONES_HEAD_DOWN = {
    '2' : (255, 295),
    '4' : (200, 255),
    '6' : (100, 200),
    '8' : (0, 100)
}

ZONES_HEAD_ZERO = {
    '4' : (275, 300),
    '6' : (200, 275),
    '8' : (0, 200)
}

ZONES_CUR = ZONES_HEAD_ZERO

WARP_HEAD_DOWN = [[135,0],[165,0],[10,200],[310,200]]
WARP_HEAD_ZERO = [[135,120],[165,120],[10,200],[310,200]]

WARP_CUR = WARP_HEAD_ZERO

def setHeadState(self, angle : float):
    global WARP_CUR
    global ZONES_CUR
    if angle == 0:
        WARP_CUR = WARP_HEAD_ZERO
        ZONES_CUR = ZONES_HEAD_ZERO

    if angle == -25:
        WARP_CUR = WARP_HEAD_DOWN
        ZONES_CUR = ZONES_HEAD_DOWN

Robot.setHeadState = setHeadState

def detectLines(self, event, *, image: cozmo.world.CameraImage, **kw):
    
    cvIm = np.array(image.raw_image)
    # Convert RGB to BGR
    cvIm = cvIm[:, :, ::-1].copy()
    cvIm = cvIm[40:, :]
    wrp = warp(cvIm)
    storeImg(cvIm, "std")
    
    storeImg(wrp, "WARPED")
    lines = getAllLines(wrp)
    # lines = getProbablisticHoughLines(cvIm)
    h, w, z = wrp.shape
    
    visLines = {'2' : None}
    if lines is not None and len(lines) > 0:
         for line in lines:
             for h in line['lines']:
                visLines[line['zone']] = True
                y = getRealY(h, line['zone']);
                cv2.line(wrp, (0, y), (w, y), (0, 0, 255), 2)

    storeImg(wrp, "warpLines")
    self.linesInZone = visLines

Robot.detectLines = detectLines 

def getAllLines(img):
    img = prepareImage(img)
    imgs = splitAreaOfInterest(img)
    lines = []
    for x in imgs:
        lines.append({
            'lines' : findLines(imgs[x]),
            'zone' : x})
    print(lines)
    return lines



def prepareImage(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = cv2.blur(img, (4, 4))

    t, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    img = cv2.adaptiveThreshold(img, 127, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1)
    storeImg(img, "postprocess")
    return img


def storeImg(img, name = "last"):
    cv2.imwrite("data/%s.jpg" % name, img)

def warp(img):
    rows,cols,ch = img.shape

    pts1 = np.float32(WARP_CUR)


    pts2 = np.float32([[0,0],[800,0],[0,300],[800,300]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    warped = cv2.warpPerspective(img,M,(300,300))

    cv2.line(img, (WARP_CUR[0][0], WARP_CUR[0][1]), (WARP_CUR[1][0], WARP_CUR[1][1]), (255,0,0))
    cv2.line(img, (WARP_CUR[2][0], WARP_CUR[2][1]), (WARP_CUR[3][0], WARP_CUR[3][1]), (255,0,0))
    cv2.line(img, (WARP_CUR[0][0], WARP_CUR[0][1]), (WARP_CUR[2][0], WARP_CUR[2][1]), (255,0,0))
    cv2.line(img, (WARP_CUR[1][0], WARP_CUR[1][1]), (WARP_CUR[3][0], WARP_CUR[3][1]), (255,0,0))


    storeImg(img, "rect.prewarp")
    return warped

def splitAreaOfInterest(img):

    aoi = {}
    for x in ZONES_CUR:
        temp = img[ZONES_CUR[x][0]:, :]
        dif = ZONES_CUR[x][1] - ZONES_CUR[x][0]
        temp = temp[:dif, :]
        aoi[x] = temp
        storeImg(aoi[x], x)
    return aoi
        
def findLines(img):
    thresh = 200
    h, w = img.shape
    starts = []

    #use buffer to avoid measuring 'wide' lines
    buf = 0
    for y in range(h):
        if img[y][0] == 0 and buf == 0:
            starts.append(y)
            buf = 3
        if buf > 0:
            buf = buf - 1

    gapThresh = 5
    lines = []
    deltaY = 0
    for s in starts:
        yThesh = 2
        length = 0
        row = s
        gapSize = 0
        for x in range(w):
            if img[row][x] == 0:
                gapSize = 0        
                length = length + 1
            elif row != h - 1 and img[row + 1][x] == 0:
                deltaY = deltaY + 1
                gapSize = 0        
                length = length + 1
                row = row + 1                
            elif row != 1 and img[row - 1][x] == 0:     
                deltaY = deltaY - 1
                gapSize = 0        
                length = length + 1
                row = row - 1
            else:
                gapSize = gapSize + 1
                if gapSize > gapThresh:
                    break
        if length >= thresh and deltaY <= yThesh:
            lines.append(s)

    return lines

def getRealY(val, zone):

    return ZONES_CUR[zone][0] + val 