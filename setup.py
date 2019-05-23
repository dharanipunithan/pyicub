from setuptools import setup
import setuptools

setup(name='pyicub',
      version='0.1',
      description='iCub Python Wrapper',
      url='http://github.com/s4hri/pyicub',
      author='Davide De Tommaso',
      author_email='davide.detommaso@iit.it',
      license='GPLv3',
#      packages=['pyicub'],
      packages=setuptools.find_packages(),
      zip_safe=False)
