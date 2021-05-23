# from constraint.node.SubstitutorVisitor import SubstitutorVisitor


class Node(object):
    def __init__(self):
        self.children = list()



class LEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' <= ' + str(self.children[1]) + ')'


class GEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)
    def __str__(self):
        return '(' + str(self.children[0]) + ' >= ' + str(self.children[1]) + ')'

class Less(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)
    def __str__(self):
        return '(' + str(self.children[0]) + ' < ' + str(self.children[1]) + ')'

class Greater(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)
    def __str__(self):
        return '(' + str(self.children[0]) + ' > ' + str(self.children[1]) + ')'


class EQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' = ' + str(self.children[1]) + ')'


class NEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' != ' + str(self.children[1]) + ')'


class In(Node):
    def __init__(self, op, op_low, op_up):
        Node.__init__(self)
        self.children.append(op)
        self.children.append(op_low)
        self.children.append(op_up)

    def __str__(self):
        return '(' + str(self.children[0]) +  ')' + ' IN ' + '[ ' + str(self.children[1]) + ' , ' + str(self.children[2]) + ' ]'



class Variable(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name

    def __str__(self):
        return self.name


class Constant(Node):
    def __init__(self, value):
        Node.__init__(self)
        self.value = value

    def __str__(self):
        return str(self.value)


class Addition(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' + ' + str(self.children[1]) + ')'


class Subtraction(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' - ' + str(self.children[1]) + ')'

class Multiplication(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)

    def __str__(self):
        return '(' + str(self.children[0]) + ' * ' + str(self.children[1]) + ')'


class Exponential(Node):
    def __init__(self, op1):
        Node.__init__(self)
        self.children.append(op1)

    def __str__(self):
        return '(' + 'EXP(' +  str(self.children[1]) + ') ' + ')'

