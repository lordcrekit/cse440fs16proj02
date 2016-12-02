"""
Parses the tokenized file/string into an Abstract Syntax Tree.
"""
import ply.yacc as yacc;
from lexer import tokens;
import lexer;
import ast as ast;

def p_start(p): "start : relation eols attributes eols data"; p[0] = ast.Source(p[1], p[2], p[3]);

# Relation
def p_relation(p): "relation : RELATION id"; p[0] = ast.Relation(p[2]);

# Attributes
def p_attributes(p): "attributes : attribute"; p[0] = [p[1]];
def p_attributes_many(p): "attributes : attributes attribute"; pass;

def p_attribute(p): "attribute : ATTRIBUTE id LBRACE options RBRACE"; pass;

# Data
def p_data(p): "data : DATA datapoints"; p[0] = p[2];
def p_datapoints(p): "datapoints : datapoint"; p[0] = [p[1]];
def p_datapoints_many(p): "datapoints : datapoint EOL datapoints"; pass;
def p_datapoint(p): "datapoint : options";

# IDs

def getParser(debug=False):
    lexer.getLexer();
    if debug:
        parser = yacc.yacc();
    else:
        parser = yacc.yacc(errorlog=yacc.NullLogger());
    return parser;

