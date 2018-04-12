from setuptools import setup

setup(
    name = 'OSU-Cozmo-Library',
    version = '0.1',
    description = 'Wrapper library for the cozmo api',
    url = 'https://github.com/OSU-cozmo/OSU-Cozmo-Library',
    license = 'MIT',
    packages = ['OSUCozmoLibrary'],
    install_requires=['cozmo[camera]'],
    zip_safe = True)
