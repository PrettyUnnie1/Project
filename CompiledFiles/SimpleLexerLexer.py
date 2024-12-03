# Generated from Sample.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\4")
        buf.write("\26\b\1\4\2\t\2\4\3\t\3\3\2\6\2\t\n\2\r\2\16\2\n\3\2\5")
        buf.write("\2\16\n\2\3\3\6\3\21\n\3\r\3\16\3\22\3\3\3\3\2\2\4\3\3")
        buf.write("\5\4\3\2\4\4\2C\\c|\5\2\13\f\17\17\"\"\2\30\2\3\3\2\2")
        buf.write("\2\2\5\3\2\2\2\3\r\3\2\2\2\5\20\3\2\2\2\7\t\t\2\2\2\b")
        buf.write("\7\3\2\2\2\t\n\3\2\2\2\n\b\3\2\2\2\n\13\3\2\2\2\13\16")
        buf.write("\3\2\2\2\f\16\t\2\2\2\r\b\3\2\2\2\r\f\3\2\2\2\16\4\3\2")
        buf.write("\2\2\17\21\t\3\2\2\20\17\3\2\2\2\21\22\3\2\2\2\22\20\3")
        buf.write("\2\2\2\22\23\3\2\2\2\23\24\3\2\2\2\24\25\b\3\2\2\25\6")
        buf.write("\3\2\2\2\6\2\n\r\22\3\b\2\2")
        return buf.getvalue()


class SimpleLexerLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    WORD = 1
    WS = 2

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
 ]

    symbolicNames = [ "<INVALID>",
            "WORD", "WS" ]

    ruleNames = [ "WORD", "WS" ]

    grammarFileName = "Sample.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


