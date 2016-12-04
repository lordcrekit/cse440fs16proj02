"""
Tokenizes the input file/string.
"""
import ply.lex as lex;

# Actual functions
def getLexer():
    return lex.lex();


# The lexer stuff.
tokens = ["RELATION", "ATTRIBUTE", "DATA", "ID", "COMMA", "LBRACE", "RBRACE", "EOL"];

def t_EOL(t): r'\n+'; t.lexer.lineno += len(t.value); return t;

def t_RELATION(t): r'@relation\b'; return t;
def t_ATTRIBUTE(t): r'@attribute\b'; return t;
def t_DATA(t): r'@data\b'; return t;

def t_COMMA(t): r','; return t;
def t_LBRACE(t): r'{'; return t;
def t_RBRACE(t): r'}'; return t;
def t_ID(t): r'[a-zA-Z][a-zA-Z0-9]*'; return t;

# Comments and shit
def t_comment(t): r'%.*'; pass;
t_ignore = ' \t';

# Errors
def t_error(t): raise Exception("Unknown token on line %s: %s" % (t.lineno, t.value[0]));

