#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#
# Copyright (C) 2015 Chase McManning <cmcmanning@gmail.com>
#
# License TODO
#

from setuptools import setup

PACKAGE = 'osutractheme'

setup(
    name = 'OSUTracTheme',
    version = '0.1.0',
    packages = [PACKAGE],

    author = 'Chase McManning',
    author_email = 'cmcmanning@gmail.com',
    description = 'Trac theme for the OSU Office of Research that complies with university style guidelines',
    license = 'TODO',
    zip_safe = True,

    install_requires = [
        'Trac',
        'TracThemeEngine>=2.0'
    ]

    entry_points = {
        'trac.plugins': 'OSUTracTheme = %s' % (PACKAGE)
    }
)