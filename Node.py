__author__ = 'Sabrout'


class Node:
    """Class represents the attributes of a Node"""

    def __init__(self, state, parent_node, operator_type, depth, path_cost):
        self.state = state
        self.parent_node = parent_node
        self.operator_type = operator_type
        self.depth = depth
        self.path_cost = path_cost

