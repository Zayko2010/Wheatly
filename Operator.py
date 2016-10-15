import Direction
from State import State
from Node import Node
from Cell import Cell
from enum import Enum
__author__ = 'Sabrout'


class Operator(Enum):
    """Class defines the operators to apply on the node.states"""

    Move = 1
    Right = 2
    Left = 3
    Back = 4

    @staticmethod
    def move(node):
        if node.state.ori == Direction.Direction.East:
            node.state.cell.x += 1
        elif node.state.ori == Direction.Direction.North:
            node.state.cell.y += 1
        elif node.state.ori == Direction.Direction.West:
            node.state.cell.x -= 1
        elif node.state.ori == Direction.Direction.South:
            node.state.cell.y -= 1

        'Zaki: Check if the cell has pokemons to catch them'
        print("Operator Move Executed")

    @staticmethod
    def turn_right(node):
        if node.state.ori == Direction.Direction.East:
            node.state.ori = Direction.Direction.South
        elif node.state.ori == Direction.Direction.North:
            node.state.ori = Direction.Direction.East
        elif node.state.ori == Direction.Direction.West:
            node.state.ori = Direction.Direction.North
        elif node.state.ori == Direction.Direction.South:
            node.state.ori = Direction.Direction.West

    @staticmethod
    def turn_left(node):
        if node.state.ori == Direction.Direction.East:
            node.state.ori = Direction.Direction.North
        elif node.state.ori == Direction.Direction.North:
            node.state.ori = Direction.Direction.West
        elif node.state.ori == Direction.Direction.West:
            node.state.ori = Direction.Direction.South
        elif node.state.ori == Direction.Direction.South:
            node.state.ori = Direction.Direction.East

    @staticmethod
    def turn_back(node):
        if node.state.ori == Direction.Direction.East:
            node.state.ori = Direction.Direction.West
        elif node.state.ori == Direction.Direction.North:
            node.state.ori = Direction.Direction.South
        elif node.state.ori == Direction.Direction.West:
            node.state.ori = Direction.Direction.East
        elif node.state.ori == Direction.Direction.South:
            node.state.ori = Direction.Direction.North


'Test'
initial_cell = Cell(1, 1, False, False)
initial_state = State(initial_cell, Direction.Direction.North, 0)
initial_node = Node(initial_state, None, None, 0, 0)
Operator.move(initial_node)
print(str(initial_cell))