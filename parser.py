"""
Parses the tokenized file/string into an Abstract Syntax Tree.
"""
import ply.yacc as yacc;
from lexer import tokens;
import lexer;
import ast as ast;

def p_start(p): "start : eol_opt relation eol_opt attributes eol_opt data eol_opt"; p[0] = ast.Source(p[2], p[4], p[6]);

# Relation
def p_relation(p): "relation : RELATION id"; p[0] = ast.Relation(p[2]);

# Attributes
def p_attributes(p): "attributes : attribute"; p[0] = [p[1]];
def p_attributes_many(p): "attributes : attributes eol attribute"; p[1].append(p[3]); p[0] = p[1];
def p_attribute(p): "attribute : ATTRIBUTE id LBRACE options RBRACE"; p[0] = ast.Attribute(p[2], p[4]);

# Data
def p_data(p): "data : DATA eol datapoints"; p[0] = p[3];
def p_datapoints(p): "datapoints : datapoint"; p[0] = [p[1]];
def p_datapoints_many(p): "datapoints : datapoints eol datapoint"; p[0] = p[1]; p[0].append(p[3]);
def p_datapoint(p): "datapoint : options"; p[0] = ast.Data(p[1]);

# Options
def p_options(p): "options : id"; p[0] = [p[1]];
def p_options_many(p): "options : options COMMA id"; p[1].append(p[3]); p[0] = p[1];

# ID
def p_id(p): "id : ID"; p[0] = ast.ID(p[1]);

# EOL
def p_eol_optional(p): "eol_opt : eol"; p[0] = "EOL";
def p_eol_optional_empty(p): "eol_opt : "; p[0] = "EOL";
def p_eol(p): "eol : EOL"; p[0] = "EOL";
def p_eol_many(p): "eol : eol EOL"; p[0] = "EOL";

def getParser(debug=False):
    lexer.getLexer();
    if debug:
        parser = yacc.yacc();
    else:
        parser = yacc.yacc(errorlog=yacc.NullLogger());
    return parser;

#def p_error(p): raise Exception("Invalid file. Failed on %s" % (p,));
