#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 04.07.2017 20:02
:Licence MIT
Part of grammpy

"""
from unittest import TestCase, main

from grammpy.old_api import Terminal


class TempClass:
    pass


class TerminalCreationTest(TestCase):
    def test_createWithSymbol(self):
        ter = Terminal('a')
        self.assertEqual('a', ter.symbol(), 'Terminal should return same symbol')

    def test_createWithNumber(self):
        ter = Terminal(5)
        self.assertEqual(5, ter.symbol(), 'Terminal should return same number')

    def test_createWithClass(self):
        ter = Terminal(TempClass)
        self.assertEqual(TempClass, ter.symbol(), 'Terminal should return same class')

    def test_createWithInstance(self):
        inst = TempClass()
        ter = Terminal(inst)
        self.assertEqual(inst, ter.symbol(), 'Terminal should return same instance')

if __name__ == '__main__':
    main()