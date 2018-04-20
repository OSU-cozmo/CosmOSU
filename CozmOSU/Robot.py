import cozmo

class Robot:
    robot = False
    _startOn = False

    def start(self, startOn):
        self._startOn = startOn
        cozmo.run_program(self._begin)

    def _begin(self, cozmo):
        self.robot = cozmo
        self._startOn(self)