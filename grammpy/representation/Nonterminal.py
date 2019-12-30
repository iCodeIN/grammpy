#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 28.07.2017 09:14
:Licence MIT
Part of grammpy

"""

from inspect import isclass
from .support._RuleConnectable import _RuleConnectable


class Nonterminal(_RuleConnectable):
    '''
    Base class that represents nonterminals.
    '''

    @staticmethod
    def is_nonterminal(var):
        # TODO comments
        return isclass(var) and issubclass(var, Nonterminal)
