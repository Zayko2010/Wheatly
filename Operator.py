import Direction
from State import State
from Node import Node
from Cell import Cell
# import Search
__author__ = 'Sabrout'


class Operator:
    """Class defines the operators to apply on the node.states"""
    def __init__(self):
        self.type = 1

    @staticmethod
    def move(maze, node):
        maze.grid[0][2].has_poke = True
        print("Maze from Operator has_poke[0][2]: {0}".format(maze.grid[0][2].has_poke))

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
# initial_cell = Cell(1, 1, False, False)
# initial_state = State(initial_cell, Direction.Direction.North, 0)
# initial_node = Node(initial_state, None, None, 0, 0)
# move(initial_node)
# print(str(initial_cell))