#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.08.2017 17:24
:Licence MIT
Part of grammpy

"""
from typing import Any

from .LLException import LLException


class DuplicateEntryException(LLException):
    """
    Some error connected to LL parsing.
    """

    def __init__(self, at_stack, see, rule, previous_rule, table) -> None:
        super().__init__()
        self.at_stack = at_stack
        self.see = see
        self.rule = rule
        self.previous_rule = previous_rule
        self.table = table


