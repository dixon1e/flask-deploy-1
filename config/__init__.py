#!/usr/bin/env python

import os
import sys
import config.settings

# create settings object corresponding to env
APP_ENV = os.environ.get('APP_ENV','Dev')

# N.B. To understand the following, first look at the file config/settings.py
# that file contains any or all "working environments" for the programmer
# this code selects one of the words "DevConfig, TestConfig or ProductionConfig"
# This chooses the  "environment" by, which the author usually means Dev, Test or Prod
# Result: _current will contain all the ENV variables found in the APP_ENV environment configuration
# 
_current = getattr(sys.modules['config.settings'], '{0}Config'.format(APP_ENV))()

# Loop through all the ENV vars found for the working environment
for atr in [f for f in dir(_current) if not '__' in f]:
    # environment can override anything
    val = os.environ.get(atr, getattr(_current, atr))
    setattr(sys.modules[__name__], atr, val)

def as_dict():
    res = {}
    for atr in [f for f in dir(config) if not '__' in f]:
        val = getattr(config, atr)
        res[atr] = val
    return res
