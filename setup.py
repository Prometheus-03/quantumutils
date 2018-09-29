# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='quantumutils',
    version='0.0.1',
    description='A simple utility for discord.py rewrite',
    long_description=readme,
    author='Prometheus',
    author_email='vengat2905@gmail.com',
    url='https://github.com/SVengat03/quantumutils',
    license=license,
    packages=find_packages(exclude=('docs'))
)
