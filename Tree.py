__author__ = 'Sabrout'
from Cell import Cell
from State import State
from Direction import Direction
from Node import Node


class Tree:
    """The class represents the attributes of a Tree"""

    def __init__(self):
        initial_cell = Cell(1, 1, False, False)
        initial_state = State(initial_cell, Direction.East, 0)
        self.root = Node(initial_state, None, None, 0, 0)
        q = list()
        q.append(self.root)