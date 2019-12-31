#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 30.12.2019 20:34
:Licence MIT
Part of grammpy

"""

# source: https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/

from timeit import default_timer as timer
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree, Traversing
from grammpy.parsers import ll, cyk
class E(Nonterminal): pass
class E2(Nonterminal): pass
class T(Nonterminal): pass
class T2(Nonterminal): pass
class F(Nonterminal): pass
class R1(Rule): rule = ([E], [T, E2])
class R2(Rule): rule = ([E2], ['+', T, E2])
class R3(Rule): rule = ([E2], [EPS])
class R4(Rule): rule = ([T], [F, T2])
class R5(Rule): rule = ([T2], ['*', F, T2])
class R6(Rule): rule = ([T2], [EPS])
class R7(Rule): rule = ([F], [0])
class R8(Rule): rule = ([F], ['(', E, ')'])


class ArithmeticTest(TestCase):

    def test_arithmetic_plus(self):
        g = Grammar(start_symbol=E,
                    terminals=[0, '(', ')', '+', '*'],
                    nonterminals=[E, E2, T, T2, F],
                    rules=[R1, R2, R3, R4, R5, R6, R7, R8])
        t = ContextFree.create_ll_table(g)
        root = ll(g, t, [0, '+', '(', 0, '+', 0, '*', 0, ')', '*', 0])
        print(Traversing.print(root))


if __name__ == '__main__':
    main()
