from anyHR.constraint.node.Node import *
from anyHR.constraint.node.SubstitutorVisitor import SubstitutorVisitor
from typing import Dict

def substitute(node:Node, var_val_pairs: Dict[str, float]):
    substitutor = SubstitutorVisitor(node)
    substitutor.substitute(var_val_pairs)