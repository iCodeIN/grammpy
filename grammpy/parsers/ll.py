#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 31.12.2019 10:30
:Licence MIT
Part of grammpy

"""
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from grammpy import *  # pragma: no cover

from ..exceptions import NoRuleForViewException
from ..representation import Nonterminal, Terminal, EPSILON
from ..transforms import Manipulations

def ll(grammar, table, input, view=1):
    root = grammar.start()  # type: Nonterminal
    stack = [root]
    stream = iter(input)
    symbol, index = next(stream), 0
    while len(stack) > 0:
        try:
            if not isinstance(stack[-1], Nonterminal):
                if stack[-1].s is EPSILON:
                    stack.pop()
                    continue
                if hash(stack[-1]) != hash(symbol):
                    raise Exception()  # TODO custom exception
                new_term = symbol if isinstance(symbol, Terminal) else Terminal(symbol)
                Manipulations.replaceNode(stack[-1], new_term)
                try:
                    symbol, index = next(stream), index + 1
                except StopIteration:
                    symbol, index = EPSILON, index + 1
                stack.pop()
                continue
            rule_to_use = table[type(stack[-1]), symbol]
            rule = rule_to_use()  # type: Rule
            parent_node = stack[-1]  # type: Nonterminal
            stack.pop()
            parent_node._set_to_rule(rule)
            rule._from_symbols.append(parent_node)
            child_nodes = list(map(
                lambda x: x() if Nonterminal.is_nonterminal(x) else (x if isinstance(x, Terminal) else Terminal(x)),
                rule.right
            ))
            for ch in child_nodes:
                ch._set_from_rule(rule)
                rule._to_symbols.append(ch)
            for ch in reversed(child_nodes):
                stack.append(ch)
        except NoRuleForViewException as e:
            # TODO
            raise
    return root