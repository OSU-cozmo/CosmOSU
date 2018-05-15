from ..Robot import Robot
import numpy as np
import cv2
import cozmo 

class line:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2
        
    def getSlope(self):
        dx = self.x2 - self.x1
        dy = self.y2 - self.y2
        if dx is 0:
            return "V"
        if dy is 0:
            return "H"
        return dy/dx
    def __str__(self):

        return "(%d, %d) (%d, %d) slope : %s\n" % (self.x1, self.y1, self.x2, self.y2, self.getSlope())
    
    def __repr__(self):
        
        return self.__str__()

def detectLines(self, event, *, image: cozmo.world.CameraImage, **kw):
    cvIm = np.array(image.raw_image)
    # Convert RGB to BGR
    cvIm = cvIm[:, :, ::-1].copy()
    lines = getHoughLines(cvIm)
    # lines = getProbablisticHoughLines(cvIm)
    print(lines)

Robot.detectLines = detectLines 

def getHoughLines(img):

    img = prepareImage(img)
    
    lines = cv2.HoughLines(img, 1, np.pi/180, 200)
    lineArr = []
    if lines is not None:
        for x in lines:
            for rho, theta in x:
                a = np.cos(theta)
                b = np.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                lineArr.append(line(x1, y1, x2, y2))
                #cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
    return lineArr

def getProbablisticHoughLines(img, minLen = 100, maxGap = 10):

    img = prepareImage(img)

    lines = cv2.HoughLinesP(img, 1, np.pi/180, 100, minLen, maxGap)

    lineArr = []
    if lines is not None:
        for x in lines:
            for x1, y1, x2, y2 in x:
                lineArr.append(line(x1,y1,x2,y2))
    return lineArr

def prepareImage(img):

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    img = cv2.adaptiveThreshold(img, 127, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1)
    
    img = img[10:, 10:]

    edges = cv2.Canny(img, 50, 150, apertureSize=3)
    return edges
