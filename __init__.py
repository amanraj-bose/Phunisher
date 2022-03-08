#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from main import set
from os import system
from builtins import print, KeyboardInterrupt, Exception, ImportError, AttributeError, OSError

try:
    classes = set()
    classes.__Main_Over__()
except KeyboardInterrupt and Exception and ImportError and AttributeError and OSError:
     print("")
     system("clear")