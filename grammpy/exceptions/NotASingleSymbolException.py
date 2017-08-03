#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""

from .CannotConvertException import CannotConvertException


class NotASingleSymbolException(CannotConvertException):
    def __init__(self, symbols):
        self.symbols = symbols