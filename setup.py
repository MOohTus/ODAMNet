from setuptools import setup, find_packages

# Read the contents of the README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / 'README.rst').read_text()

setup(name='EnvironmentProject',
      version = '1.0', 
      packages=find_packages(),
      long_description=long_description)
