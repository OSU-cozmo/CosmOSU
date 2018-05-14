from ..Robot import Robot


def enableCamera(self,  viewer : bool = False, bool : color = True,):
    self.kwargDict['use_viewer'] = viewer
    self.kwargDict['force_viewer_on_top'] = viewer
    self.startEvts.append((startSettings, (color))

Robot.enableCamera = enableCamera

def getCozmoCamera():
    return self.robot.world.camera()

Robot.getCozmoCamera = getCozmoCamera

def startSettings(color):
    robot.camera.image_stream_enabled = True
    robot.camera.color_image_enabled = color
