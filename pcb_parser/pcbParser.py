# Generated from pcb.g by ANTLR 4.7
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO
import sys

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3")
        buf.write(u"\7\26\4\2\t\2\4\3\t\3\3\2\3\2\3\2\7\2\n\n\2\f\2\16\2")
        buf.write(u"\r\13\2\3\2\3\2\3\3\3\3\3\3\5\3\24\n\3\3\3\2\2\4\2\4")
        buf.write(u"\2\2\2\26\2\6\3\2\2\2\4\23\3\2\2\2\6\7\7\3\2\2\7\13\7")
        buf.write(u"\6\2\2\b\n\5\4\3\2\t\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2")
        buf.write(u"\2\13\f\3\2\2\2\f\16\3\2\2\2\r\13\3\2\2\2\16\17\7\4\2")
        buf.write(u"\2\17\3\3\2\2\2\20\24\7\6\2\2\21\24\7\5\2\2\22\24\5\2")
        buf.write(u"\2\2\23\20\3\2\2\2\23\21\3\2\2\2\23\22\3\2\2\2\24\5\3")
        buf.write(u"\2\2\2\4\13\23")
        return buf.getvalue()


class pcbParser ( Parser ):

    grammarFileName = "pcb.g"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'('", u"')'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"STRING", 
                      u"WORD", u"WS" ]

    RULE_node = 0
    RULE_content = 1

    ruleNames =  [ u"node", u"content" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    STRING=3
    WORD=4
    WS=5

    def __init__(self, input, output=sys.stdout):
        super(pcbParser, self).__init__(input, output=output)
        self.checkVersion("4.7")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class NodeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(pcbParser.NodeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(pcbParser.WORD, 0)

        def content(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(pcbParser.ContentContext)
            else:
                return self.getTypedRuleContext(pcbParser.ContentContext,i)


        def getRuleIndex(self):
            return pcbParser.RULE_node

        def enterRule(self, listener):
            if hasattr(listener, "enterNode"):
                listener.enterNode(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitNode"):
                listener.exitNode(self)




    def node(self):

        localctx = pcbParser.NodeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_node)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 4
            self.match(pcbParser.T__0)
            self.state = 5
            self.match(pcbParser.WORD)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << pcbParser.T__0) | (1 << pcbParser.STRING) | (1 << pcbParser.WORD))) != 0):
                self.state = 6
                self.content()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(pcbParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ContentContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(pcbParser.ContentContext, self).__init__(parent, invokingState)
            self.parser = parser

        def WORD(self):
            return self.getToken(pcbParser.WORD, 0)

        def STRING(self):
            return self.getToken(pcbParser.STRING, 0)

        def node(self):
            return self.getTypedRuleContext(pcbParser.NodeContext,0)


        def getRuleIndex(self):
            return pcbParser.RULE_content

        def enterRule(self, listener):
            if hasattr(listener, "enterContent"):
                listener.enterContent(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitContent"):
                listener.exitContent(self)




    def content(self):

        localctx = pcbParser.ContentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_content)
        try:
            self.state = 17
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [pcbParser.WORD]:
                self.enterOuterAlt(localctx, 1)
                self.state = 14
                self.match(pcbParser.WORD)
                pass
            elif token in [pcbParser.STRING]:
                self.enterOuterAlt(localctx, 2)
                self.state = 15
                self.match(pcbParser.STRING)
                pass
            elif token in [pcbParser.T__0]:
                self.enterOuterAlt(localctx, 3)
                self.state = 16
                self.node()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





