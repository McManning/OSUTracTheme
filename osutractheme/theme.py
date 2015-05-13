#!/usr/bin/env python
# -*- coding: utf-8 -*-
#

#
# Copyright (C) 2015 Chase McManning <cmcmanning@gmail.com>
#
# License TODO
#

from trac.core import *
from themeengine.api import ThemeBase

class OSUTracTheme(ThemeBase):
    """Trac theme for OSU Office of Research """
    template = htdocs = css = True
