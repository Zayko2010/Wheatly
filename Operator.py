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
        output_state = None
        'Integer represents if the next cell has a pokemon'
        output_has_poke = 0
        if node.state.ori == Direction.Direction.East:
            if maze.grid[node.state.cell.x + 1][node.state.cell.y].has_poke:
                output_has_poke = 1
            output_state = State(maze.grid[node.state.cell.x + 1][node.state.cell.y], node.state.ori, node.state.pok_so_far + output_has_poke)
            return Node(output_state, node, node.depth + 1, node.path_cost + 1)

        elif node.state.ori == Direction.Direction.North:
            if maze.grid[node.state.cell.x][node.state.cell.y + 1].has_poke:
                output_has_poke = 1
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y + 1], node.state.ori, node.state.pok_so_far + output_has_poke)
            return Node(output_state, node, node.depth + 1, node.path_cost + 1)

        elif node.state.ori == Direction.Direction.West:
            if maze.grid[node.state.cell.x - 1][node.state.cell.y].has_poke:
                output_has_poke = 1
            output_state = State(maze.grid[node.state.cell.x - 1][node.state.cell.y], node.state.ori, node.state.pok_so_far + output_has_poke)
            return Node(output_state, node, node.depth + 1, node.path_cost + 1)

        elif node.state.ori == Direction.Direction.South:
            if maze.grid[node.state.cell.x][node.state.cell.y - 1].has_poke:
                output_has_poke = 1
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y - 1], node.state.ori, node.state.pok_so_far + output_has_poke)
            return Node(output_state, node, node.depth + 1, node.path_cost + 1)

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