#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 30.12.2019 18:01
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree
from grammpy.exceptions import NoRuleForViewException

class S(Nonterminal): pass
class A(Nonterminal): pass
class B(Nonterminal): pass
class R1(Rule): rule = ([S], [A, 'a'])
class R2(Rule): rule = ([S], ['b', S])
class R3(Rule): rule = ([A], ['c', A, 'd'])
class R4(Rule): rule = ([A], [B])
class R5(Rule): rule = ([B], ['f', S])
class R6(Rule): rule = ([B], [EPS])


class ExampleFromPresentationTest(TestCase):

    def test_one_rule(self):
        g = Grammar(start_symbol=S,
                    terminals='abcdf',
                    nonterminals=[S, A, B],
                    rules=[R1, R2, R3, R4, R5, R6])
        t = ContextFree.create_ll_table(g)
        self.assertEqual(t.stack(S).see('a'), R1)
        self.assertEqual(t.stack(A).see('a'), R4)
        self.assertEqual(t.stack(B).see('a'), R6)
        self.assertEqual(t.stack(S).see('b'), R2)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(A).see('b')
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(B).see('b')
        self.assertEqual(t.stack(S).see('c'), R1)
        self.assertEqual(t.stack(A).see('c'), R3)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(B).see('c')
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(S).see('d')
        self.assertEqual(t.stack(A).see('d'), R4)
        self.assertEqual(t.stack(B).see('d'), R6)
        self.assertEqual(t.stack(S).see('f'), R1)
        self.assertEqual(t.stack(A).see('f'), R4)
        self.assertEqual(t.stack(B).see('f'), R5)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(A).see(EPS)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(A).see(EPS)
        with self.assertRaises(NoRuleForViewException):
            _ = t.stack(A).see(EPS)


if __name__ == '__main__':
    main()
