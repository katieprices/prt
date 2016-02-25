# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='prt',
    version='1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'yaml',
    ],
    entry_points='''
        [console_scripts]
        prt=scripts.prt:main
    ''',
)
