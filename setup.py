from setuptools import setup
from setuptools import find_packages

setup(name='gym_Rubiks_Cube',
      version='0.0.1',
      install_requires=['gym', 'termcolor'],
      url="https://github.com/andresmore/gym-Rubiks-Cube",
      new_step_api=True,
      packages=find_packages()
)  
