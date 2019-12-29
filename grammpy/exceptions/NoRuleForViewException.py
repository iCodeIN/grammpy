#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:25
:Licence MIT
Part of grammpy

"""

from .LLException import LLException


class NoRuleForViewException(LLException, ValueError):
    """
    In the LL table is no rule for current symbol at the stack and view.
    """

    def __init__(self, at_stack, see, table):
        super().__init__()
        self.at_stack = at_stack
        self.see = see
        self.table = table
