#!/usr/bin/env python
"""
:Author Patrik Valkovic
:Created 30.12.2019 20:34
:Licence MIT
Part of grammpy

"""

# source: http://pages.cs.wisc.edu/~fischer/cs536.f13/lectures/f12/Lecture22.4up.pdf

from unittest import TestCase, main
from grammpy import *
from grammpy.transforms import ContextFree
from grammpy.exceptions import NoRuleForViewException

class Prog(Nonterminal): pass
class Stmts(Nonterminal): pass
class Stmt(Nonterminal): pass
class Expr(Nonterminal): pass
class Etail(Nonterminal): pass
class EOF: pass
class ID: pass
class IF: pass
class R1(Rule): rule=([Prog], ['{', Stmts, '}', EOF])
class R2(Rule): rule=([Stmts], [Stmt, Stmts])
class R3(Rule): rule=([Stmts], [EPS])
class R4(Rule): rule=([Stmt], [ID, '=', Expr, ';'])
class R5(Rule): rule=([Stmt], [IF, '(', Expr, ')', Stmt])
class R6(Rule): rule=([Expr], [ID, Etail])
class R7(Rule): rule=([Etail], ['+', Etail])
class R8(Rule): rule=([Etail], ['-', Etail])
class R9(Rule): rule=([Etail], [EPS])


class ExampleFromPresentationTest(TestCase):

    def test_one_rule(self):
        g = Grammar(start_symbol=Prog,
                    terminals=[EOF, ID, IF, '}', '{', '=', '(', ')', '+', '-', ';'],
                    nonterminals=[Prog, Stmts, Stmt, Expr, Etail],
                    rules=[R1, R2, R3, R4, R5, R6, R7, R8, R9])
        t = ContextFree.create_ll_table(g)
        self.assertEqual(t[Prog, '{'], R1)
        self.assertEqual(t[Stmts, ID], R2)
        self.assertEqual(t[Stmts, IF], R2)
        self.assertEqual(t[Stmts, '}'], R3)
        self.assertEqual(t[Stmt, ID], R4)
        self.assertEqual(t[Stmt, IF], R5)
        self.assertEqual(t[Expr, ID], R6)
        self.assertEqual(t[Etail, '+'], R7)
        self.assertEqual(t[Etail, '-'], R8)
        self.assertEqual(t[Etail, ')'], R9)
        self.assertEqual(t[Etail, ';'], R9)


if __name__ == '__main__':
    main()
