#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 10:04
:Licence MIT
Part of grammpy

"""

from .GrammpyException import GrammpyException


class NotRuleException(GrammpyException, TypeError):
    """
    Passed something else than Rule class
    """
    def __init__(self, rule):
        super().__init__()
        self.object = rule
