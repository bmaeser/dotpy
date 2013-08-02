#!/usr/bin/env python
# -*- coding: utf-8 -*-

import dotpy
from setuptools import setup, find_packages

install_requires = [
    'docopt',
]

entry_points = {
    'console_scripts': [
        'dotpy = dotpy.main:main',
    ]
}

packages = find_packages()


setup(
    name='dotpy',
    version=dotpy.__version__,
    author='Bernhard Maeser',
    author_email='bernhard.maeser@gmail.com',
    url='https://github.com/bmaeser/vol',
    license="MIT",
    description=".dotfiles distribution management",
    long_description=open('README.rst').read(),
    packages = packages,
    include_package_data=True,
    install_requires = install_requires,
    zip_safe=False,
    entry_points=entry_points,
    classifiers=(
        'Development Status :: 1 - Planning',
        'Operating System :: POSIX',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: System :: Archiving :: Packaging',
        'Topic :: System :: Shells',
        'Topic :: System :: Software Distribution',
        'Topic :: Terminals',
        'Topic :: Utilities',
    ),
)
