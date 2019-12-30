#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 30.12.2019 12:53
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main
from grammpy import *
from grammpy.transforms.LLTable.create_ll_table import _LLTable
from grammpy.exceptions import NoRuleForViewException, DuplicateEntryException

class S(Nonterminal): pass
class A(Nonterminal): pass
class R(Rule):
    rule = ([S], [0, 1])
class R2(Rule):
    rule = ([S], [0, 2])

class OneRuleTest(TestCase):

    def test_one_rule(self):
        t = _LLTable()
        t.add(S, [0], R)
        self.assertEqual(t[S, 0], R)
        self.assertEqual(t.stack(S).see(0), R)
        self.assertEqual(t.stack(S)[0], R)
        self.assertEqual(t[S, 0, 1], R)
        self.assertEqual(t.stack(S).see(0, 1), R)
        self.assertEqual(t.stack(S)[0, 1], R)
        self.assertEqual(t[S, 0], R)
        self.assertEqual(t.stack(S).see(0), R)
        self.assertEqual(t.stack(S)[0], R)
        self.assertEqual(t[S, 0, 1, 2], R)
        self.assertEqual(t.stack(S).see(0, 1, 2), R)
        self.assertEqual(t.stack(S)[0, 1, 2], R)
        with self.assertRaises(NoRuleForViewException):
            _ = t[S, 1]
        with self.assertRaises(NoRuleForViewException):
            t.stack(S).see(1)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(S)[1]

    def test_add_rule_twice(self):
        t = _LLTable()
        with self.assertRaises(DuplicateEntryException):
            t.add(S, [0], R).add(S, [0], R2)

    def test_add_same_rule_twice(self):
        t = _LLTable()
        t.add(S, [0], R).add(S, [0], R)
        self.assertEqual(t[S, 0], R)
        self.assertEqual(t.stack(S).see(0), R)
        self.assertEqual(t.stack(S)[0], R)
        self.assertEqual(t[S, 0, 1], R)
        self.assertEqual(t.stack(S).see(0, 1), R)
        self.assertEqual(t.stack(S)[0, 1], R)
        self.assertEqual(t[S, 0], R)
        self.assertEqual(t.stack(S).see(0), R)
        self.assertEqual(t.stack(S)[0], R)
        self.assertEqual(t[S, 0, 1, 2], R)
        self.assertEqual(t.stack(S).see(0, 1, 2), R)
        self.assertEqual(t.stack(S)[0, 1, 2], R)
        with self.assertRaises(NoRuleForViewException):
            _ = t[S, 1]
        with self.assertRaises(NoRuleForViewException):
            t.stack(S).see(1)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(S)[1]

    def test_symbol_not_in_table(self):
        t = _LLTable()
        t.add(S, [0], R)
        with self.assertRaises(NoRuleForViewException):
            _ = t[A, 0]
        with self.assertRaises(NoRuleForViewException):
            t.stack(A).see(0)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(A)[0]


if __name__ == '__main__':
    main()