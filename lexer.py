"""
Tokenizes the input file/string.
"""
import ply.lex as lex;

tokens = [RELATION, ATTRIBUTE];

def t_RELATION = r'\b@relation\b'; return t;
def t_ATTRIBUTE = r'\b@attribute\b'; return t;
def t_DATA = r'\b@data\b'; return t;


def t_COMMA = r','; return t;
def t_LBRACE = r'{'; return t;
def t_RBRACE = r'}'; return t;
def t_ID = r'[a-zA-Z]+'; return t;

def t_comment = r'%.*'; pass;

def t_error(t): raise Exception("Unknown token on line %s: %s" % (t.lineno, t.value[0]));

def getLexer():
    return lex.lex();
