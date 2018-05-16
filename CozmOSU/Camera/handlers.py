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

        return "(%d, %d) (%d, %d) slope : %s" % (self.x1, self.y1, self.x2, self.y2, self.getSlope())
    
    def __repr__(self):
        
        return self.__str__()

def detectLines(self, event, *, image: cozmo.world.CameraImage, **kw):
    
    cvIm = np.array(image.raw_image)
    # Convert RGB to BGR
    cvIm = cvIm[:, :, ::-1].copy()
    cvIm = cvIm[40:, :]
    wrp = warp(cvIm)
    storeImg(cvIm, "std")
    
    storeImg(wrp, "WARPED")
    lines = getHoughLines(wrp)
    # lines = getProbablisticHoughLines(cvIm)
    if len(lines) > 0:
        for x in lines:
            cv2.line(wrp, (x.x1, x.y1), (x.x2, x.y2), (0, 0, 255), 2)
            
        print(lines)
    storeImg(wrp, "warpLines")

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
    # img = cv2.blur(img, (4, 4))

    t, img = cv2.threshold(img, 200, 255, cv2.THRESH_BINARY)
    img = cv2.adaptiveThreshold(img, 127, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 1)
    storeImg(img, "post process")

    edges = cv2.Canny(img, t-10, t+10)
    storeImg(edges, "edges")
    return edges

def storeImg(img, name = "last"):
    cv2.imwrite("data/%s.jpg" % name, img)

def warp(img):
    rows,cols,ch = img.shape

    pts1 = np.float32([[135,0],[165,0],[10,200],[310,200]])



    pts2 = np.float32([[0,0],[800,0],[0,300],[800,300]])

    M = cv2.getPerspectiveTransform(pts1,pts2)

    warped = cv2.warpPerspective(img,M,(300,300))
    
    cv2.line(img, (135, 0), (165,0), (255,0,0))
    cv2.line(img, (165, 0), (310,195), (255,0,0))
    cv2.line(img, (10, 195), (310,195), (255,0,0))
    cv2.line(img, (135, 0), (10,195), (255,0,0))


    storeImg(img, "rect.prewarp")
    return warped