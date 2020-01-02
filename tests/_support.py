#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 02.01.2020 16:37
:Licence MIT
Part of grammpy

"""

from typing import Type, List, Union
from grammpy import *

def build_tree(node, rule = None, children = None):
    # type: (Type[Nonterminal, any], Type[Rule], List[Union[Nonterminal, Terminal]]) -> Nonterminal
    if Nonterminal.is_nonterminal(node):
        node_instance = node()  # type: Nonterminal
    elif isinstance(node, Terminal):
        node_instance = node
    else:
        node_instance = Terminal(node)
    if rule is not None:
        rule_instance = rule()  # type: Rule
        rule_instance._from_symbols.append(node_instance)
        node_instance._set_to_rule(rule_instance)
    for ch in children or []:
        ch._set_from_rule(rule_instance)
        rule_instance._to_symbols.append(ch)
    return node_instance