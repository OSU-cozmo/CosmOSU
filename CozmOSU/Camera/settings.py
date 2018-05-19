from ..Robot import Robot
import cozmo

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
    self.robot.camera.set_manual_exposure(67, 3)

Robot.createLineBinding = createLineBinding