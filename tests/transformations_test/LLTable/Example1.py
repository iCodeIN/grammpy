#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 30.12.2019 20:34
:Licence MIT
Part of grammpy

"""

# source: https://www.geeksforgeeks.org/construction-of-ll1-parsing-table/

from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree
from grammpy.exceptions import NoRuleForViewException

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


class ExampleFromPresentationTest(TestCase):

    def test_one_rule(self):
        g = Grammar(start_symbol=E,
                    terminals=[0, '(', ')', '+', '*'],
                    nonterminals=[E, E2, T, T2, F],
                    rules=[R1, R2, R3, R4, R5, R6, R7, R8])
        t = ContextFree.create_ll_table(g)
        self.assertEqual(t[E, 0], R1)
        self.assertEqual(t[E, '('], R1)
        self.assertEqual(t[E2, '+'], R2)
        self.assertEqual(t[E2, ')'], R3)
        self.assertEqual(t[E2, EPS], R3)
        self.assertEqual(t[T, 0], R4)
        self.assertEqual(t[T, '('], R4)
        self.assertEqual(t[T2, '+'], R6)
        self.assertEqual(t[T2, '*'], R5)
        self.assertEqual(t[T2, ')'], R6)
        self.assertEqual(t[T2, EPS], R6)
        self.assertEqual(t[F, 0], R7)
        self.assertEqual(t[F, '('], R8)
        with self.assertRaises(NoRuleForViewException):
            _ = t[E, '+']
        with self.assertRaises(NoRuleForViewException):
            _ = t[E, '*']
        with self.assertRaises(NoRuleForViewException):
            _ = t[E, ')']
        with self.assertRaises(NoRuleForViewException):
            _ = t[E, EPS]
        with self.assertRaises(NoRuleForViewException):
            _ = t[E2, 0]
        with self.assertRaises(NoRuleForViewException):
            _ = t[E2, '*']
        with self.assertRaises(NoRuleForViewException):
            _ = t[E2, '(']
        with self.assertRaises(NoRuleForViewException):
            _ = t[T, '+']
        with self.assertRaises(NoRuleForViewException):
            _ = t[T, '*']
        with self.assertRaises(NoRuleForViewException):
            _ = t[T, ')']
        with self.assertRaises(NoRuleForViewException):
            _ = t[T, EPS]
        with self.assertRaises(NoRuleForViewException):
            _ = t[T2, 0]
        with self.assertRaises(NoRuleForViewException):
            _ = t[T2, '(']
        with self.assertRaises(NoRuleForViewException):
            _ = t[F, '+']
        with self.assertRaises(NoRuleForViewException):
            _ = t[F, '*']
        with self.assertRaises(NoRuleForViewException):
            _ = t[F, ')']
        with self.assertRaises(NoRuleForViewException):
            _ = t[F, EPS]


if __name__ == '__main__':
    main()
