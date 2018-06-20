from os import path

from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

setup(
    name='lab10',
    version='0.0.1',
    license='MIT',
    description='Lab10 - package management',
    long_description=open('README.rst').read(),
    url='https://github.com/hvvka/packaging-jenkins',
    author='Hanna',
    author_email='226154@student.pwr.edu.pl',
    packages=find_packages(exclude=['tests*'])
)
