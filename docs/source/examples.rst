Examples
********

.. toctree::
   :maxdepth: 2
   :caption: Contents:


Hello World
===========
  A basic hello world program.

  .. code-block:: python

    import CozmOSU as Robot

    robot = Robot.Robot();

    def main(cozmo : Robot.Robot):

        cozmo.say("Hello World");

    robot.start(main);

Speech
======

    Basic speech examples.


    .. code-block:: python
        
        import CozmOSU

        def main(robot):
            robot.say("Hello World")

            #Say The sum of 5 plus 5 is 10
            robot.sayMath("The sum of %d + %d is %d" % (5, 5, 5 + 5))

            # Say 5 minus 10 
            robot.sayMath("%d - %d is %d" % (5, 10, 5 - 10))

        robot = CozmOSU.Robot()

        robot.start(main)

Recording Pitch
===============

    Record the pitch (incline) or the robot.

    .. code-block:: python
        
        import CozmOSU

        def main(robot):

            robot.calibrateLevelPitch()

            deltaTime = 0.1
            outFile = "pitch-data.txt"

            robot.recordPitch(outFile, deltaTime)


            robot.turn(360)

        robot = CozmOSU.Robot()
        robot.start(main)



Light Cube Gradient
===================

    Create a rainbow gradient and cycle through on lightcubes.

    .. code-block:: python

        import CozmOSU

        from CozmOSU.helpers import buildGradient
        from time import sleep

        def main(robot):

            res = 20

            red = (255, 0, 0)
            aqua = (0, 255, 255)
            
            rainbow = buildGradient(res, red, aqua) + buildGradient(res, aqua, red)

            loc = 0
            timeToRun = 30
            elapsed = 0

            while elapsed <= timeToRun:

                robot.setCubeColor(1, rainbow[loc % len(rainbow)])
                robot.setCubeColor(2, rainbow[(loc + 1) % len(rainbow)])
                robot.setCubeColor(3, rainbow[(loc + 2)% len(rainbow)])
                
                loc += 1

                sleep(0.1)
                elapsed += 0.1


        robot = CozmOSU.Robot()
        robot.start(main)
