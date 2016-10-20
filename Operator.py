import Direction
from State import State
from Node import Node
from OperatorType import OperatorType
# import Search
__author__ = 'Sabrout'


class Operator:
    """Class defines the operators to apply on the node.states"""
    def __init__(self):
        self.type = 0

    @staticmethod
    def move(maze, node):
        """Integer represents if the next cell has a pokemon"""
        output_has_poke = 0
        if node.state.ori == Direction.Direction.East:
            if not node.state.cell.y + 1 > maze.grid.__len__():
                if not maze.grid[node.state.cell.y + 1][node.state.cell.x].is_wall:
                    if maze.grid[node.state.cell.y + 1][node.state.cell.x].has_poke:
                        output_has_poke = 1
                    output_state = State(maze.grid[node.state.cell.y + 1][node.state.cell.x], node.state.ori, node.state.pok_so_far + output_has_poke)
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        elif node.state.ori == Direction.Direction.North:
            if not node.state.cell.x - 1 < 0:
                if not maze.grid[node.state.cell.y][node.state.cell.x - 1].is_wall:
                    if maze.grid[node.state.cell.y][node.state.cell.x - 1].has_poke:
                        output_has_poke = 1
                    output_state = State(maze.grid[node.state.cell.y][node.state.cell.x - 1], node.state.ori, node.state.pok_so_far + output_has_poke)
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        elif node.state.ori == Direction.Direction.West:
            if not node.state.cell.x - 1 < 0:
                if not maze.grid[node.state.cell.y - 1][node.state.cell.x].is_wall:
                    if maze.grid[node.state.cell.y - 1][node.state.cell.x].has_poke:
                        output_has_poke = 1
                    output_state = State(maze.grid[node.state.cell.y - 1][node.state.cell.x], node.state.ori, node.state.pok_so_far + output_has_poke)
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        elif node.state.ori == Direction.Direction.South:
            if not node.state.cell.x + 1 > maze.grid.__len__():
                if not maze.grid[node.state.cell.y][node.state.cell.x + 1].is_wall:
                    if maze.grid[node.state.cell.y][node.state.cell.x + 1].has_poke:
                        output_has_poke = 1
                    output_state = State(maze.grid[node.state.cell.y][node.state.cell.x + 1], node.state.ori, node.state.pok_so_far + output_has_poke)
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        print("ERROR")

    @staticmethod
    def turn_right(maze, node):
        if node.state.ori == Direction.Direction.East:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.South, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.North:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.East, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.West:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.North, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.South:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.West, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

    @staticmethod
    def turn_left(maze, node):
        if node.state.ori == Direction.Direction.East:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.North, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.North:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.West, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.West:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.South, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.South:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.East, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

    @staticmethod
    def turn_back(maze, node):
        if node.state.ori == Direction.Direction.East:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.West, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.North:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.South, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.West:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.East, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.South:
            output_state = State(maze.grid[node.state.cell.y][node.state.cell.x], Direction.Direction.North, node.state.pok_so_far)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)


'Test'
# initial_cell = Cell(1, 1, False, False)
# initial_state = State(initial_cell, Direction.North, 0)
# initial_node = Node(initial_state, None, None, 0, 0)
# move(initial_node)
# print(str(initial_cell))