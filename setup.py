# -*- coding: utf-8 -*-
import sys

from setuptools import setup

PACKAGE = 'cwlogs'
SOURCE = './'
with open('VERSION') as f:
    VERSION = f.read().rstrip()

REQUIRES = [
]

with open('requirements.txt') as f:
    REQUIRES.append(f.read().rstrip())

setup(
    name=PACKAGE,
    version=VERSION,
    py_modules=[PACKAGE],
    entry_points={
    'console_scripts': ['%s = %s:main' % (PACKAGE, PACKAGE)],},
    install_requires=REQUIRES,
)
