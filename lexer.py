"""
Tokenizes the input file/string.
"""
import ply.lex as lex;

tokens = ["RELATION", "ATTRIBUTE"];

def t_RELATION(t): r'\b@relation\b'; return t;
def t_ATTRIBUTE(t): r'\b@attribute\b'; return t;
def t_DATA(t): r'\b@data\b'; return t;


def t_COMMA(t): r','; return t;
def t_LBRACE(t): r'{'; return t;
def t_RBRACE(t): r'}'; return t;
def t_ID(t): r'[a-zA-Z]+'; return t;

def t_comment(t): r'%.*'; pass;

def t_error(t): raise Exception("Unknown token on line %s: %s" % (t.lineno, t.value[0]));

def getLexer():
    return lex.lex();
