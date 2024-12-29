# Generated from D:\IU\Year4_Sem1\Priciples\Final_Project\Project\Sample.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .SampleParser import SampleParser
else:
    from SampleParser import SampleParser

# This class defines a complete listener for a parse tree produced by SampleParser.
class SampleListener(ParseTreeListener):

    # Enter a parse tree produced by SampleParser#sentence.
    def enterSentence(self, ctx:SampleParser.SentenceContext):
        pass

    # Exit a parse tree produced by SampleParser#sentence.
    def exitSentence(self, ctx:SampleParser.SentenceContext):
        pass


    # Enter a parse tree produced by SampleParser#word.
    def enterWord(self, ctx:SampleParser.WordContext):
        pass

    # Exit a parse tree produced by SampleParser#word.
    def exitWord(self, ctx:SampleParser.WordContext):
        pass



del SampleParser