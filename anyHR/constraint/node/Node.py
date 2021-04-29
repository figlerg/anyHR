class Node(object):
    def __init__(self):
        self.children = list()


class LEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class GEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class Less(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class Greater(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class EQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class NEQ(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class In(Node):
    def __init__(self, op, op_low, op_up):
        Node.__init__(self)
        self.children.append(op)
        self.children.append(op_low)
        self.children.append(op_up)


class Variable(Node):
    def __init__(self, name):
        Node.__init__(self)
        self.name = name


class Constant(Node):
    def __init__(self, value):
        Node.__init__(self)
        self.value = value


class Addition(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class Subtraction(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class Multiplication(Node):
    def __init__(self, op1, op2):
        Node.__init__(self)
        self.children.append(op1)
        self.children.append(op2)


class Exponential(Node):
    def __init__(self, op1):
        Node.__init__(self)
        self.children.append(op1)


# LRA_LEQ DONE
# LRA_GEQ DONE
# LRA_Less -
# LRA_Greater -
# LRA_Eq -
# LRA_Neq -
# LRA_In -
# ExpressionVariable DONE
# ExpressionConstant DONE
# ExpressionParanthesis NOT NEEDED?
# ExpressionExponential
# ExpressionMultiplication
# ExpressionAddition DONE
# ExpressionSubtraction
