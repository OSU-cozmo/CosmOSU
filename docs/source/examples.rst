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


Others
======
