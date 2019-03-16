#!/usr/bin/env python3
#  -*- coding: utf-8 -*-
from distutils.core import setup, Extension

module1 = Extension('simple_graphs',
                    sources = ['SimpleGraph.c'])

setup (name = 'PackageName',
       ext_modules = [module1])
