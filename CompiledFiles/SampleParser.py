# Generated from Sample.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\6")
        buf.write("\20\4\2\t\2\4\3\t\3\3\2\6\2\b\n\2\r\2\16\2\t\3\2\3\2\3")
        buf.write("\3\3\3\3\3\2\2\4\2\4\2\3\3\2\3\5\2\16\2\7\3\2\2\2\4\r")
        buf.write("\3\2\2\2\6\b\5\4\3\2\7\6\3\2\2\2\b\t\3\2\2\2\t\7\3\2\2")
        buf.write("\2\t\n\3\2\2\2\n\13\3\2\2\2\13\f\7\2\2\3\f\3\3\2\2\2\r")
        buf.write("\16\t\2\2\2\16\5\3\2\2\2\3\t")
        return buf.getvalue()


class SampleParser ( Parser ):

    grammarFileName = "Sample.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [  ]

    symbolicNames = [ "<INVALID>", "POSITIVE", "NEGATIVE", "OTHER", "WS" ]

    RULE_sentence = 0
    RULE_word = 1

    ruleNames =  [ "sentence", "word" ]

    EOF = Token.EOF
    POSITIVE=1
    NEGATIVE=2
    OTHER=3
    WS=4

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class SentenceContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(SampleParser.EOF, 0)

        def word(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(SampleParser.WordContext)
            else:
                return self.getTypedRuleContext(SampleParser.WordContext,i)


        def getRuleIndex(self):
            return SampleParser.RULE_sentence




    def sentence(self):

        localctx = SampleParser.SentenceContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_sentence)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 5 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 4
                self.word()
                self.state = 7 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.POSITIVE) | (1 << SampleParser.NEGATIVE) | (1 << SampleParser.OTHER))) != 0)):
                    break

            self.state = 9
            self.match(SampleParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def POSITIVE(self):
            return self.getToken(SampleParser.POSITIVE, 0)

        def NEGATIVE(self):
            return self.getToken(SampleParser.NEGATIVE, 0)

        def OTHER(self):
            return self.getToken(SampleParser.OTHER, 0)

        def getRuleIndex(self):
            return SampleParser.RULE_word




    def word(self):

        localctx = SampleParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_word)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 11
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << SampleParser.POSITIVE) | (1 << SampleParser.NEGATIVE) | (1 << SampleParser.OTHER))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





