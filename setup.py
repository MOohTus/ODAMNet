from setuptools import setup, find_packages

from main import __version__

# Read the contents of the README file
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / 'README.rst').read_text()

setup(name='EnvironmentProject',
      version=__version__,
      author='Morgane Térézol',
      author_email='morgane.terezol@univ-amu.fr',
      description='Study the link between environmental factors and rare diseases',
      packages=find_packages(),
      long_description=long_description,
      license='MIT',
      python_requires='>=3.9',
      classifiers=[
            'Programming Language :: Python :: 3.9',
            'Programming Language :: Python :: 3',
            'License :: OSI Approved :: MIT License',
            'Operating System :: OS Independent',
      ],
      url='https://github.com/MOohTus/EnvironmentProject',
      keywords=[
            'rare diseases',
            'overlap',
            'WikiPathways',
            'chemicals',
            'pathways overlap',
            'pathways diffusion',
            'active module identification',
            'random walk with restart',
            'RWR',
            'AMI',
            'EJP-RD'
      ],
      zip_safe=True)
