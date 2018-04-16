import cozmo
from .Actions import Actions
from .Drive import Drive

class Robot (Actions, Drive):
    robot = False
    _startOn = False

    def __init__(self):
        print("Robot Class init finished")

    def start(self, startOn):
        self._startOn = startOn
        cozmo.run_program(self._begin)

    def _begin(self, cozmo):
        self.robot = cozmo
        self._startOn(self)
