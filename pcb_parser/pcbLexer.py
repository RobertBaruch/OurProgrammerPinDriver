# Generated from pcb.g by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2")
        buf.write(u"\7,\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t")
        buf.write(u"\7\3\2\3\2\3\3\3\3\3\4\3\4\3\4\7\4\27\n\4\f\4\16\4\32")
        buf.write(u"\13\4\3\4\3\4\3\5\3\5\3\5\3\6\6\6\"\n\6\r\6\16\6#\3\7")
        buf.write(u"\6\7\'\n\7\r\7\16\7(\3\7\3\7\3\30\2\b\3\3\5\4\7\5\t\2")
        buf.write(u"\13\6\r\7\3\2\5\7\2$$^^ppttvv\7\2\13\f\17\17\"\"$$*+")
        buf.write(u"\5\2\13\f\17\17\"\"\2.\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3")
        buf.write(u"\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\3\17\3\2\2\2\5\21\3\2")
        buf.write(u"\2\2\7\23\3\2\2\2\t\35\3\2\2\2\13!\3\2\2\2\r&\3\2\2\2")
        buf.write(u"\17\20\7*\2\2\20\4\3\2\2\2\21\22\7+\2\2\22\6\3\2\2\2")
        buf.write(u"\23\30\7$\2\2\24\27\5\t\5\2\25\27\13\2\2\2\26\24\3\2")
        buf.write(u"\2\2\26\25\3\2\2\2\27\32\3\2\2\2\30\31\3\2\2\2\30\26")
        buf.write(u"\3\2\2\2\31\33\3\2\2\2\32\30\3\2\2\2\33\34\7$\2\2\34")
        buf.write(u"\b\3\2\2\2\35\36\7^\2\2\36\37\t\2\2\2\37\n\3\2\2\2 \"")
        buf.write(u"\n\3\2\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2\2$\f")
        buf.write(u"\3\2\2\2%\'\t\4\2\2&%\3\2\2\2\'(\3\2\2\2(&\3\2\2\2()")
        buf.write(u"\3\2\2\2)*\3\2\2\2*+\b\7\2\2+\16\3\2\2\2\7\2\26\30#(")
        buf.write(u"\3\b\2\2")
        return buf.getvalue()


class pcbLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    STRING = 3
    WORD = 4
    WS = 5

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>",
            u"STRING", u"WORD", u"WS" ]

    ruleNames = [ u"T__0", u"T__1", u"STRING", u"ESCAPED", u"WORD", u"WS" ]

    grammarFileName = u"pcb.g"

    def __init__(self, input=None, output=sys.stdout):
        super(pcbLexer, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


