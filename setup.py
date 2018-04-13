from setuptools import setup

setup(
    name = 'CosmOSU',
    version = '0.1',
    description = 'Wrapper library for the cozmo api',
    url = 'https://github.com/OSU-cozmo/OSU-Cozmo-Library',
    license = 'MIT',
    packages = ['CozmOSU'],
    install_requires=['cozmo[camera]'],
    zip_safe = True)
