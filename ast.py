"""
Abstract representation of the project.
"""

class AstNode(object):
    def __init__(self): pass;
    def interpret(self): raise NotImplementedError();
    def __repr__(self): return self.__str__();
    def __str__(self): return "%s%s" % ("name", "contents");
