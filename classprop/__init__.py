# -*- coding: utf-8 -*-

"""Top-level package for classprop."""

__author__ = """romnnn"""
__email__ = "contact@romnn.com"
__version__ = "0.1.0"

from classprop.classprop import ClassPropertyMetaClass as _mc
from classprop.classprop import class_property

# Aliases
class_prop = class_property
classprop = class_property
classproperty = class_property
ClassPropertyMetaClass = _mc
