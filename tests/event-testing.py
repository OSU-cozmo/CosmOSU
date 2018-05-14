import CozmOSU
import cozmo

def handled(evt, state):
    print("Event Correctly Dispatched")



def main(robot : CozmOSU.Robot):
    robot.bindEvent(cozmo.objects.EvtObjectTapped, handled)

    while True:
        pass


robot = CozmOSU.Robot()

robot.start(main)