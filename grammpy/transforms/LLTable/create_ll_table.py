#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 29.12.2019 23:33
:Licence MIT
Part of grammpy

"""

from typing import TYPE_CHECKING, Type, Iterable, Union

if TYPE_CHECKING:
    from grammpy import *  # pragma: no cover

from ...exceptions import NoRuleForViewException, DuplicateEntryException
from ...representation import EPSILON, Nonterminal


# TODO COMMENTS, Type hinting


class _LLTableQuery:
    def __init__(self, table, at_stack):
        #  type: (_LLTable, Type[Nonterminal]) -> _LLTableQuery
        self._table = table  # type: _LLTable
        self._at_stack = at_stack  # type: Type[Nonterminal]

    def __getitem__(self, see):
        see = see if isinstance(see, Iterable) else [see]
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
        see = tuple(see if isinstance(see, Iterable) else [see])
        self._distance = max(self.distance, len(see))
        at_stack_dict = dict.setdefault(self._map, hash(at_stack), dict())
        see_h = hash(see)
        if see_h in at_stack_dict and at_stack_dict[see_h] != rule:
            raise DuplicateEntryException(at_stack, see, rule, at_stack_dict[see_h], self)
        at_stack_dict[see_h] = rule
        return self

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


def _first_over_sequence(sequence, first):
    f = set()
    symb_f = [EPSILON]
    for symb in sequence:
        symb_f = dict.setdefault(first, symb, set())
        if symb == EPSILON:
            symb_f.add(EPSILON)
        f = f.union(symb_f - {EPSILON})
        if EPSILON not in symb_f:
            return f
    if EPSILON in symb_f:
        f.add(EPSILON)
    return f


def create_ll_table(grammar, distance=1):
    # type: (Grammar, int) -> _LLTable
    # TODO doc comment
    # Compute first set
    first = dict()
    something_changed = True
    while something_changed:
        something_changed = False
        for rule in grammar.rules:
            l = rule.fromSymbol  # type: Type[Nonterminal]
            r = rule.right  # type: list
            new_s = dict.setdefault(first, l, set()).copy()
            for r_part in r:
                r_set = None
                if r_part == EPSILON:
                    new_s.add(EPSILON)
                    r_set = [EPSILON]
                    break
                if not Nonterminal.is_nonterminal(r_part):
                    new_s.add(r_part)
                    break
                r_set = dict.setdefault(first, r_part, set())
                new_s = new_s.union(r_set)
                if EPSILON not in r_set:
                    break
                new_s.remove(EPSILON)
            if r_set is not None and EPSILON in r_set:
                new_s.add(EPSILON)
            something_changed = something_changed or new_s != first[l]
            first[l] = new_s
    # fill terminals to first
    for t in grammar.terminals:
        first[t] = {t}
    # compute follow set
    follow = dict()
    follow[grammar.start] = {EPSILON}
    something_changed = True
    while something_changed:
        something_changed = False
        for rule in grammar.rules:
            l = rule.fromSymbol  # type: Type[Nonterminal]
            r = rule.right  # type: list
            # part 1
            for symb, index in zip(r, range(len(r))):
                if not Nonterminal.is_nonterminal(symb):
                    continue
                right_first = _first_over_sequence(r[index + 1:], first)
                new_s = dict.setdefault(follow, symb, set()) | (right_first - {EPSILON})
                if EPSILON in right_first:
                    new_s = new_s | dict.setdefault(follow, l, set())
                something_changed = something_changed or new_s != follow[symb]
                follow[symb] = new_s
    # cosntruct the table
    table = _LLTable()
    for rule in grammar.rules:
        r_first = _first_over_sequence(rule.right, first)
        for can_be in r_first - {EPSILON}:
            table.add(rule.fromSymbol, [can_be], rule)
        if EPSILON in r_first:
            for can_be in follow[rule.fromSymbol]:
                table.add(rule.fromSymbol, [can_be], rule)
    return table
