#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 29.12.2019 23:41
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree
from grammpy.exceptions import NoRuleForViewException

class S(Nonterminal): pass
class R(Rule):
    rule = ([S], [0, 1])

class OneRuleTest(TestCase):

    def test_one_rule(self):
        g = Grammar(start_symbol=S,
                    terminals=[0, 1],
                    nonterminals=[S],
                    rules=[R])
        t = ContextFree.create_ll_table(g)
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


if __name__ == '__main__':
    main()
