from ..Robot import Robot
import cozmo
import os
import time 
def enableCamera(self,  viewer : bool = False, color : bool = True):
    self.kwargDict['use_viewer'] = viewer
    self.kwargDict['force_viewer_on_top'] = viewer
    callafter = {
        "function" : self.cameraInit, 
        "params": (color,)
    }
    self.startEvts.append(callafter)
    self.linesInZone = None

Robot.enableCamera = enableCamera

def cameraInit(self, color):
    self.robot.camera.image_stream_enabled = True
    self.robot.camera.color_image_enabled = color

Robot.cameraInit = cameraInit


def watchForLines(self, range : int = 1):
    callafter = {
        "function" : self.createLineBinding, 
        "params": (range,)
    }
    self.startEvts.append(callafter)

Robot.watchForLines = watchForLines

def createLineBinding(self, range : int = 1):

    self.robot.add_event_handler(cozmo.world.EvtNewCameraImage, self.detectLines)
    if not self.importSettings():
        self.log.error('No Calibration settings found, please run calibration in local')
        self.log.error('the accuracy of the line detection')
        return
    self.log.info('Setting exposure to : %d' % self.exposure)
    self.log.info('Setting Gain to : %2.1f'% self.gain)
    self.robot.camera.set_manual_exposure(self.exposure, self.gain)
    # self.robot.camera.enable_auto_exposure(True)
Robot.createLineBinding = createLineBinding

def calibrateExposure(self, accuracy: float = 0.8, start : int = 1):
    self.log.info('Initializing')
    self.log.info('If no lines are in Cozmo\'s field of view, results will be eraneous\n')
    time.sleep(1)
    self.log.info('Starting to calibrate exposure')
    exp = start
    gain = [1, 1.5, 2, 2.5, 3]
    useExp = False
    step = 0
    lines = None
    self.areLinesVisible() # reset the current lines
    while exp < 67:
        self.robot.camera.set_manual_exposure(exp, gain[step])
        time.sleep(1)
        lines = self.areLinesVisible()
        count = 0
        if lines is not None:
            for x in lines:
                if x > 275:
                    count = count + 1

        if count > (accuracy * self.lineIterations):
            break
        self.lineIterations = 0
        if useExp:
            exp = exp + 1
            useExp = False
        else:
            step = step + 1
            if step >= len(gain):
                step = 0
                useExp = True
        

    self.exposure = exp
    self.gain = gain[step]
    self.exportSettings()
    return lines, exp, gain[step]

Robot.calibrateExposure = calibrateExposure

def calibrateToLine(self, accuracy = 0.8):
    self.moveLift(0)
    self.moveHead(0)
    self.driveForward(-60, 50)
    self.moveLift(1)
    lines, exposure, gain = self.calibrateExposure(accuracy)
    self.log.info("found lines %s, with exposure %d, and gain %2.1f" % (lines, exposure, gain))

Robot.calibrateToLine = calibrateToLine


def exportSettings(self):
    if self.exposure not in range(0, 68):
        self.log.error("Could not calibrate the exposure, try to verify a line")
        self.log.error("is in cozmo's field of view")
    file = open('.settings.cozmo', 'w')

    file.write('EXPOSURE:%d\n' % self.exposure)
    file.write('GAIN:%f\n' % self.gain)
    file.close()

Robot.exportSettings = exportSettings

def importSettings(self):
    if not os.path.isfile('.settings.cozmo'):
        return False
    file = open('.settings.cozmo', 'r')
    for line in file.readlines():
        if 'EXPOSURE' in line:
            self.exposure = int(line.split(':')[1])
            print('Found exposure')
        if 'GAIN' in line:
            self.gain = float(line.split(':')[1])
            print('Found gain')
            
    file.close
    return True

Robot.importSettings = importSettings