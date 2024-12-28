# sentiment_analyzer.py
import sys
from antlr4 import *
from CompiledFiles.SampleLexer import SampleLexer
from CompiledFiles.SampleParser import SampleParser
from SampleListenerImpl import SampleListenerImpl
from antlr4.error.ErrorListener import ErrorListener

class CustomErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"Syntax Error at line {line}, column {column}: {msg}")
        # Optionally, you can raise an exception or handle the error as needed

class SentimentAnalyzer:
    def __init__(self):
        self.listener = SampleListenerImpl()

    def analyze(self, input_sentence):
        """
        Analyzes the sentiment of the input_sentence.

        Parameters:
            input_sentence (str): The sentence to analyze.

        Returns:
            str: The sentiment result ("Positive", "Negative", "Mixed", "Neutral").
        """
        # Reset the listener's sentiment flags
        self.listener.reset()

        # Convert input to lowercase for case insensitivity
        input_sentence = input_sentence.lower()

        # Initialize the input stream
        input_stream = InputStream(input_sentence)

        # Initialize the lexer
        lexer = SampleLexer(input_stream)

        # Generate tokens
        token_stream = CommonTokenStream(lexer)

        # Initialize the parser
        parser = SampleParser(token_stream)

        # Remove default error listeners and add custom error listener
        parser.removeErrorListeners()
        parser.addErrorListener(CustomErrorListener())

        # Parse the sentence starting from the 'sentence' rule
        try:
            tree = parser.sentence()
        except Exception as e:
            print(f"Parsing Error: {e}")
            return "Error"

        # Walk the parse tree with the listener
        walker = ParseTreeWalker()
        walker.walk(self.listener, tree)

        # Determine sentiment
        sentiment = self.listener.get_sentiment()

        return sentiment
