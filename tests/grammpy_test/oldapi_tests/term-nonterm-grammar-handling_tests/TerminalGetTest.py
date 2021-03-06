#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 03.08.2017 12:28
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy.old_api import Grammar


class TempClass:
    pass


class TerminalGetTest(TestCase):
    def test_getTermEmpty(self):
        gr = Grammar()
        self.assertIsNone(gr.get_term(TempClass))
        self.assertIsNone(gr.get_term(1))
        self.assertIsNone(gr.get_term('asdf'))

    def test_getTermClass(self):
        gr = Grammar()
        gr.add_term(TempClass)
        self.assertEqual(gr.get_term(TempClass).s, TempClass)

    def test_getTermArray(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        g = gr.get_term([0, 'asdf'])
        for i in g:
            self.assertTrue(i.s in [TempClass, 0, 'asdf'])
        self.assertEqual(g[0].s, 0)
        self.assertEqual(g[1].s, 'asdf')

    def test_dontGetTermArray(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        g = gr.get_term([TempClass, 'a'])
        self.assertEqual(g[0].s, TempClass)
        self.assertIsNone(g[1])

    def test_getTermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        g = gr.get_term((0, 'asdf'))
        for i in g:
            self.assertTrue(i.s in [TempClass, 0, 'asdf'])
        self.assertEqual(g[0].s, 0)
        self.assertEqual(g[1].s, 'asdf')

    def test_dontGetTermTuple(self):
        gr = Grammar()
        gr.add_term([TempClass, 0, 'asdf'])
        g = gr.get_term((TempClass, 'a'))
        self.assertEqual(g[0].s, TempClass)
        self.assertIsNone(g[1])

if __name__ == '__main__':
    main()