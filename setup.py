#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import absolute_import
from setuptools import setup, find_packages
import codecs
import os
import re
import sys


def read(*parts):
    path = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(path, encoding='utf-8') as fobj:
        return fobj.read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


install_requires = [
    'docker-compose >= 1.2, < 2',
    'Jinja2 >= 2.7, < 3',
]



setup(
    name='meta-compose',
    version=find_version("metacompose", "__init__.py"),
    description='Templating wrapper for docker-compose',
    url='https://github.com/webcrofting/meta-compose',
    author='Christoph Witzany',
    license='Apache License 2.0',
    packages=find_packages(exclude=['tests.*', 'tests']),
    include_package_data=True,
    install_requires=install_requires,
    entry_points="""
    [console_scripts]
    meta-compose=metacompose.cli.main:main
    """,
)
