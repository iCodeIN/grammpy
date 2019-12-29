#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 29.12.2019 23:33
:Licence MIT
Part of grammpy

"""

from typing import TYPE_CHECKING, Type, Iterable, Union
from ...exceptions import NoRuleForViewException

if TYPE_CHECKING:
    from grammpy import *


# TODO COMMENTS, Type hinting


class _LLTableQuery:
    def __init__(self, table, at_stack):
        #  type: (_LLTable, Type[Nonterminal]) -> _LLTableQuery
        self._table = table  # type: _LLTable
        self._at_stack = at_stack  # type: Type[Nonterminal]

    def __getitem__(self, see):
        return self._table[tuple([self._at_stack] + list(see))]

    def see(self, *see):
        return self[see]


class _LLTable:
    def __init__(self):
        self._distance = 1
        self._map = dict()

    @property
    def distance(self):
        return self._distance

    def add(self, at_stack, see, rule):
        # type: (Type[Nonterminal], Iterable[Union[Type[Nonterminal], Terminal]], Type[Rule]) -> _LLTable
        see = tuple(see)
        self._distance = max(self.distance, len(see))
        at_stack_dict = dict.setdefault(self._map, hash(at_stack), dict())
        at_stack_dict[hash(see)] = rule
        pass

    def __getitem__(self, keys):
        at_stack = keys[0]
        see = keys[1:]
        at_stack_h = hash(at_stack)
        if at_stack_h not in self._map:
            raise NoRuleForViewException(at_stack, see, self)
        at_stack_dict = self._map[at_stack_h]
        for subsee in [tuple(see[:i]) for i in range(min(len('asdf'), self.distance), 0, -1)]:
            if hash(subsee) in at_stack_dict:
                return at_stack_dict[hash(subsee)]
        raise NoRuleForViewException(at_stack, see, self)

    def stack(self, at_stack):
        # type: (Type[Nonterminal]) -> _LLTableQuery
        return _LLTableQuery(self, at_stack)


def create_ll_table(grammar, distance=1):
    # type: (Grammar, int) -> _LLTable
    # TODO doc comment
    pass
