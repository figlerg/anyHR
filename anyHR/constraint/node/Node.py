# from constraint.node.SubstitutorVisitor import SubstitutorVisitor
from enum import Enum



class Node(object):
    def __init__(self):
        self.children = list()
        self.node_type = NodeType.NODE

    def get_vars(self, vars = set()):
        # recursively crawls tree and writes down all the variables

        # stop
        if self.node_type == NodeType.VARIABLE:
            vars.add(self.name)

        # recursion
        for child in self.children:
            child.get_vars(vars)

        return vars



# for visitor class. Using isinstance breaks when importing from outside
class NodeType(Enum):
    NODE = 0
    LEQ = 1
    GEQ = 2
    LESS = 3
    GREATER = 4
    EQ = 5
    NEQ = 6
    IN = 7
    VARIABLE = 8
    CONSTANT = 9
    ADDITION = 10
    SUBTRACTION = 11
    MULTIPLICATION = 12
    EXPONENTIAL = 13

    def __eq__(self, other):
        return self.value == other.value


class LEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.LEQ
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' <= ' + str(self.children[1]) + ')'


class GEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.GEQ
        self.children.append(op1)
        self.children.append(op2)
    def __str__(self):
        return '(' + str(self.children[0]) + ' >= ' + str(self.children[1]) + ')'

class Less(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.LESS
        self.children.append(op1)
        self.children.append(op2)
    def __str__(self):
        return '(' + str(self.children[0]) + ' < ' + str(self.children[1]) + ')'

class Greater(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.GREATER
        self.children.append(op1)
        self.children.append(op2)
    def __str__(self):
        return '(' + str(self.children[0]) + ' > ' + str(self.children[1]) + ')'


class EQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.EQ
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' = ' + str(self.children[1]) + ')'


class NEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.NEQ
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' != ' + str(self.children[1]) + ')'


class In(Node):
    def __init__(self, op, op_low, op_up):
        Node.__init__(self)
        self.node_type = NodeType.IN
        self.children.append(op)
        self.children.append(op_low)
        self.children.append(op_up)

    def __str__(self):
        return '(' + str(self.children[0]) +  ')' + ' IN ' + '[ ' + str(self.children[1]) + ' , ' + str(self.children[2]) + ' ]'



class Variable(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.node_type = NodeType.VARIABLE
        self.name = name

    def __str__(self):
        return self.name


class Constant(Node):
    def __init__(self, value):
        Node.__init__(self)
        self.node_type = NodeType.CONSTANT
        self.value = value

    def __str__(self):
        return str(self.value)


class Addition(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.ADDITION
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' + ' + str(self.children[1]) + ')'


class Subtraction(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.SUBTRACTION
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' - ' + str(self.children[1]) + ')'

class Multiplication(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.node_type = NodeType.MULTIPLICATION
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' * ' + str(self.children[1]) + ')'


class Exponential(Node):
    def __init__(self, op1):
        Node.__init__(self)
        self.node_type = NodeType.EXPONENTIAL
        self.children.append(op1)

    def __str__(self):
        return '(' + 'EXP(' +  str(self.children[1]) + ') ' + ')'

