import os
from setuptools import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
   name='automatic-ripping-machine',
   version='@version@',
   description='A automatic-ripping-machine',
   license="MIT",
   author='automatic-ripping-machine contributors',
   packages=['automatic-ripping-machine'],  #same as name
   install_requires=required[1:], #external packages as dependencies
)
