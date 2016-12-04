"""
Abstract representation of the project.
"""

class ID(object):
    def __init__(self, name):
        assert type(name) is str;
        self.name=name;
    def __str__(self): return self.name;
    def __repr__(self): return str(self);

class AstNode(object):
    def interpret(self, lt): raise NotImplementedError();
    def __repr__(self): return self.__str__();
    def __str__(self): return "%s%s" % (type(self).__name__,"contents");

class Source(AstNode):
    def __init__(self, relation, attributes, data):
        assert type(relation) is Relation, "got %s" % (type(relation),);
        assert type(attributes) is list;
        assert type(data) is list, "got %s" % (data,);
        self.relation = relation;
        self.attributes = attributes;
        self.data = data;
    def interpret(self, lt):
        self.relation.interpret(lt);
        for i in range(0, len(self.attributes)-1):
            self.attributes[i].interpret(lt);
        self.attributes[len(self.attributes)-1].interpret(lt, True);
        for point in self.data:
            point.interpret(lt);

class Relation(AstNode):
    def __init__(self, name):
        assert type(name) is ID;
        self.name = name;
    def interpret(self, lt):
        lt.name = self.name;

class Attribute(AstNode):
    def __init__(self, name, options):
        assert type(name) is ID;
        assert type(options) is list;
        self.name = name;
        self.options = options;
    def interpret(self, lt, isLast=False):
        if isLast:
            lt.goal = self;
        else:
            lt.attributes.append(self);
    def __str__(self): return "%s%s" % (self.name, self.options);
    def __repr__(self): return str(self);

class Data(AstNode):
    def __init__(self, data):
        assert type(data) is list;
        self.data = data[0:len(data)-1];
        self.goal = data[len(data)-1];

    def interpret(self, lt):
        if self.goal.name == "T":
            self.goal = True;
        elif self.goal.name == "F":
            self.goal = False;
        else:
            raise Exception("Expect T or F as value for datapoint Goal, not %s" % (self.goal,));
        lt.data.append(self);

    def __str__(self): return "{%s:%s}" % (self.data, self.goal);
    def __repr__(self): return str(self);

