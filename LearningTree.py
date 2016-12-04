from pprint import pformat;
from ast import Data;
import math;
import copy;

def B(q):
    assert 0 <= q <= 1;
    if q == 0 or q == 1:
        return 0;
    else:
        return -(q*math.log2(q)+(1-q)*math.log2(1-q));

def H(orig):
    p = orig.positives;
    n = orig.negatives;
    return B(p/(p+n));

def Remainder(orig, new):
    """
    Orig is the set of data before.
    new is the set of sets of data that it has been broken into.
    """
    p = orig.positives;
    n = orig.negatives;
    total = 0;
    for s in new:
        pk = s.positives;
        nk = s.negatives;
        total += ((pk+nk)/(p+n))*B(pk/(pk+nk));
    return total;

def Gain(orig, new):
    return H(orig)-Remainder(orig,new);

def splitOn(orig, number):
    output = {};
    for point in orig.data:
        point = copy.deepcopy(point);
        key = point.data.pop(number);
        if key.name not in output:
            output[key.name] = [];
        output[key.name].append(point);
    aout = {};
    for key in output:
        aout[key] = EndPoint(output[key]);

    return aout;


class LearningTree(object):
    def __init__(self):
        self.name = None;
        self.attributes = [];
        self.goal = None;
        self.data = [];

    def __str__(self):
        return "LearningTree\nname: %s\nattributes:%s\ngoal:%s\ndata:%s" \
                % (self.name, pformat(self.attributes), self.goal, pformat(self.data));
    def __repr__(self): return str(self);

    def generate_tree(self, verbose):
        assert type(verbose) is bool;
        out = EndPoint(self.data);
        out.calculate();
        return out;

indent = -1;
class EndPoint(object):
    """
    So, what we are doing is taking a set of data with attributes and splitting
        by the attribute where our Gain() is maximized. Then we do it for each
        new Endpoint that our data was split into, until we predict 100% of
        test cases.
    This class represents one Endpoint.
    """
    def __init__(self, data, verbose=True):
        assert type(data) is list, "got %s" % (type(data),);
        self.data = [];
        self.children = {};
        self.positives = 0;
        self.negatives = 0;
        for item in data:
            assert type(item) is Data, "got %s:%s" % (type(item),item);
            if item.goal:
                self.positives += 1;
            else:
                self.negatives += 1;
            self.data.append(item);


    def calculate(self, verbose=True):
        assert len(self.data) > 0;
        if self.positives == 0 or self.negatives == 0:
            return;
        current = None; # (GAIN, DATALIST)
        for i in range(0, len(self.data[0].data)):
            op = splitOn(self, i);
            for key in op:
                data = op[key];
                assert type(data) is EndPoint;
            gain = Gain(self, op.values());
            if current is None or current[0] < gain:
                current = (gain, op);
        self.children = current[1];
        #print("split on %s with gain %s" % (current[1].keys(), current[0]));
        for thing in self.children.values():
            thing.calculate(verbose);


    def __str__(self):
        return "EndPoint %s" % (pformat(self.data),);
    def __repr__(self):
        return str(self);
    def OUTPUT_STR(self):
        if self.positives == 0:
            return "F (%s)" % (len(self.data),);
        elif self.negatives == 0:
            return "T (%s)" % (len(self.data),);
        else:
            outstr = "";
            global indent;
            indent += 1;
            for key in self.children:
                outstr += "\n%s" % (' '*indent);
                if indent > 0:
                    outstr += "|";
                outstr += "%s %s" % (key, self.children[key].OUTPUT_STR());
            indent -= 1;
            return outstr;



