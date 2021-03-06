#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence MIT
Part of grammpy

"""

from unittest import TestCase, main

from grammpy.old_api import Grammar
from grammpy.old_api import Nonterminal


class TempClass(Nonterminal):
    pass


class Second(Nonterminal):
    pass


class Third(Nonterminal):
    pass


class NonterminalGetTest(TestCase):
    def test_getNontermEmpty(self):
        gr = Grammar()
        self.assertIsNone(gr.get_nonterm(TempClass))
        self.assertIsNone(gr.get_nonterm(Second))
        self.assertIsNone(gr.get_nonterm(Third))

    def test_getNontermClass(self):
        gr = Grammar()
        gr.add_nonterm(TempClass)
        self.assertEqual(gr.get_nonterm(TempClass), TempClass)

    def test_getNontermArray(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        g = gr.get_nonterm([Second, TempClass])
        for i in g:
            self.assertTrue(i in [TempClass, Second, Third])
        self.assertEqual(g[0], Second)
        self.assertEqual(g[1], TempClass)

    def test_dontGetNontermArray(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second])
        g = gr.get_nonterm([TempClass, Third])
        self.assertEqual(g[0], TempClass)
        self.assertIsNone(g[1])

    def test_getNontermTuple(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second, Third])
        g = gr.get_nonterm((Third, TempClass))
        for i in g:
            self.assertIn(i, [TempClass, Second, Third])
        self.assertEqual(g[0], Third)
        self.assertEqual(g[1], TempClass)

    def test_dontGetNontermTuple(self):
        gr = Grammar()
        gr.add_nonterm([TempClass, Second])
        g = gr.get_nonterm((TempClass, Third))
        self.assertEqual(g[0], TempClass)
        self.assertIsNone(g[1])


if __name__ == '__main__':
    main()
