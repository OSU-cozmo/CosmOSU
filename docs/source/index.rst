.. CozmOSU documentation master file, created by
   sphinx-quickstart on Tue Apr 24 18:12:02 2018.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

CozmOSU
***********


Installation
============

    Clone the repository_ to a permanant location.

    .. _repository : https://github.com/OSU-cozmo/CosmOSU

    Then in the root directory run:

    ``pip install -e .``


Hello World
=============

    .. code-block:: python


        import CozmOSU as Robot

        robot = Robot.Robot();

        def main(cozmo : Robot.Robot):

            cozmo.say("Hello World");

        robot.start(main);

Documents
=========

    .. toctree::
        :maxdepth: 2

        Robot <robot.rst>
        Actions <actions.rst>
        Driving <driving.rst>
        Sensors <sensors.rst>
        Examples <examples.rst>
        Resources <resources.rst>



Indices and tables
==================
* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
