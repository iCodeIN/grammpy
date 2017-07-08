#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 23.06.2017 16:39
:Licence GNUv3
Part of grammpy

"""
from unittest import TestCase
from grammpy.Terminal import Terminal


class TempClass:
    pass


class CorrectGrammarHandlingTest(TestCase):
    def test_sameNumber(self):
        ter1 = Terminal(0, 1)
        ter2 = Terminal(0, 1)
        self.assertEqual(ter1, ter2)

    def test_sameString(self):
        ter1 = Terminal(0, 'a')
        ter2 = Terminal(0, 'a')
        self.assertEqual(ter1, ter2)

    def test_sameClass(self):
        ter1 = Terminal(0, TempClass)
        ter2 = Terminal(0, TempClass)
        self.assertEqual(ter1, ter2)

    def test_sameInstance(self):
        inst = TempClass()
        ter1 = Terminal(0, inst)
        ter2 = Terminal(0, inst)
        self.assertEqual(ter1, ter2)