#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:24
:Licence MIT
Part of grammpy

"""

from .GrammpyException import GrammpyException


class LLException(GrammpyException):
    """
    Some error connected to LL parsing.
    """
