import cozmo
import time
def main(cozmo : cozmo.robot.Robot):
    offset = calibrateLevel(cozmo)
    print(offset)

    last = cozmo.pose_pitch.degrees - offset
    while True:
        current = cozmo.pose_pitch.degrees - offset
        if abs(last - current) > 0.5:
            last = current
            print(last)
    



def calibrateLevel(cozmo : cozmo.robot.Robot):
    print("Calibrating level")
    _sum = 0
    for x in range(10):
        _sum += cozmo.pose_pitch.degrees
        time.sleep(.1)

    return _sum/10




cozmo.run_program(main)