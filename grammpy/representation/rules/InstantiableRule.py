#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.08.2017 11:18
:Licence GNUv3
Part of grammpy

"""

from grammpy.representation.WeakList import WeakList
from .ValidationRule import ValidationRule


class InstantiableRule(ValidationRule):
    """
    Represent rule, that can be instances into AST
    """
    def __init__(self):
        self._from_symbols = WeakList()
        self._to_symbols = list()

    @property
    def from_symbols(self):
        """
        Instances of the left side of the rule
        :return: List of symbols
        """
        return list(self._from_symbols)

    @property
    def to_symbols(self):
        """
        Instances of the right side of the rule
        :return: List of symbols
        """
        return self._to_symbols