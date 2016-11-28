# Adapted from https://github.com/pypa/sampleproject/blob/master/setup.py
# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

setup(
    name='studentit-utils',
    version='0.0.1',
    description='Various utility classes for StudentIT',
    # The project's main homepage.
    url='https://github.com/cmbrad/studentit-utils',
    # Author details
    author='Christopher Bradley',
    author_email='chris.bradley@unimelb.edu.au',
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(include=['studentit*']),
)
