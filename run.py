import sys
import os
import subprocess
from antlr4 import *
from PyQt5.QtWidgets import QApplication
from UI import ChatBox  # Assuming ChatBox is in the same directory

# Define your variables
DIR = os.path.dirname(os.path.abspath(__file__))
ANTLR_JAR = 'C:\antlr\antlr4-4.9.2-complete.jar'
CPL_Dest = 'CompiledFiles'
SRC = 'Sample.g4'
TESTS = os.path.join(DIR, './tests')


def print_usage():
    print('python Hello.py gen')
    print('python Hello.py test')

def print_break():
    print('-----------------------------------------------')

def generate_antlr_to_python():
    """Function to generate ANTLR Lexer, Parser, and Listener."""
    print('Running ANTLR4...')
    cmd = [
        'java',
        '-jar',
        ANTLR_JAR,
        '-o',
        CPL_Dest,
        '-Dlanguage=Python3',
        SRC
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        print('ANTLR4 generated Lexer, Parser, and Listener successfully.')
    else:
        print('Error generating Lexer, Parser, and Listener:')
        print(result.stderr)
    print_break()

def run_test():
    """Function to run test cases."""
    print('Running testcases...')

    from CompiledFiles.SampleLexer import SampleLexer
    from CompiledFiles.SampleParser import SampleParser
    from antlr4.error.ErrorListener import ErrorListener

    class CustomErrorListener(ErrorListener):
        def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
            print(f"Input rejected: {msg}")
            exit(1)  # Exit the program with an error

    filename = '001.txt'
    input_file = os.path.join(DIR, './tests', filename)

    # Test
    input_stream = FileStream(input_file)
    lexer = SampleLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = SampleParser(stream)
    tree = parser.program()  # Start parsing at the `program` rule

    # Get all tokens
    tokens = lexer.getAllTokens()

    # Print all tokens
    print("Tokens from input:")
    for token in tokens:
        print(f"Token: {token.text}")

    # Print the parse tree (for debugging)
    print(tree.toStringTree(recog=parser))

    # Reset the input stream for parsing and catch the error
    lexer = SampleLexer(FileStream(input_file))
    token_stream = CommonTokenStream(lexer)

    parser = SampleParser(token_stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CustomErrorListener())
    try:
        parser.program()
        print("Input accepted")
    except SystemExit:
        pass

    print_break()
    print('Run tests completely')

def main(argv):
    print('Complete jar file ANTLR  :  ' + str(ANTLR_JAR))
    print('Length of arguments      :  ' + str(len(argv)))
    print_break()

    if len(argv) < 1:
        print_usage()
    elif argv[0] == 'gen':
        generate_antlr_to_python()
    elif argv[0] == 'test':
        run_test()
    elif argv[0] == 'run':
        # Initialize and run the PyQt5 application
        if not os.path.exists(CPL_Dest):
            print("CompiledFiles directory not found. Generating ANTLR files...")
            generate_antlr_to_python()

        app = QApplication(sys.argv)
        window = ChatBox()
        window.show()
        sys.exit(app.exec_())
    else:
        print_usage()

if __name__ == '__main__':
    main(sys.argv[1:])
