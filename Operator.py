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
        poks = []
        # print(node.state.pok_locations)
        if node.state.ori == Direction.Direction.East:
            if not node.state.cell.y + 1 >= maze.grid.__len__():
                if not maze.grid[node.state.cell.x][node.state.cell.y + 1].is_wall:
                    if maze.grid[node.state.cell.x][node.state.cell.y + 1].has_poke:
                        if (node.state.cell.x, node.state.cell.y + 1) not in node.state.pok_locations:
                            output_has_poke = 1
                            poks = [(node.state.cell.x, node.state.cell.y + 1)]
                            # print("poks: {0}, nodes.pok_locs: {1}".format(poks, node.state.pok_locations))
                    output_state = State(maze.grid[node.state.cell.x][node.state.cell.y + 1], node.state.ori,
                                         node.state.pok_so_far + output_has_poke, node.state.pok_locations + poks)
                    # print("output_state_poks: {0}".format(output_state.pok_locations))
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        elif node.state.ori == Direction.Direction.North:
            if not node.state.cell.x - 1 < 0:
                if not maze.grid[node.state.cell.x - 1][node.state.cell.y].is_wall:
                    if maze.grid[node.state.cell.x - 1][node.state.cell.y].has_poke:
                        if (node.state.cell.x - 1, node.state.cell.y) not in node.state.pok_locations:
                            output_has_poke = 1
                            poks = [(node.state.cell.x - 1, node.state.cell.y)]
                            # print("poks: {0}, nodes.pok_locs: {1}".format(poks, node.state.pok_locations))
                    output_state = State(maze.grid[node.state.cell.x - 1][node.state.cell.y], node.state.ori,
                                         node.state.pok_so_far + output_has_poke, node.state.pok_locations + poks)
                    # print("output_state_poks: {0}".format(output_state.pok_locations))
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        elif node.state.ori == Direction.Direction.West:
            if not node.state.cell.y - 1 < 0:
                if not maze.grid[node.state.cell.x][node.state.cell.y - 1].is_wall:
                    if maze.grid[node.state.cell.x][node.state.cell.y - 1].has_poke:
                        if (node.state.cell.x, node.state.cell.y - 1) not in node.state.pok_locations:
                            output_has_poke = 1
                            poks = [(node.state.cell.x, node.state.cell.y - 1)]
                            # print("poks: {0}, nodes.pok_locs: {1}".format(poks, node.state.pok_locations))
                        # maze.grid[node.state.cell.x][node.state.cell.y - 1].has_poke = False
                    output_state = State(maze.grid[node.state.cell.x][node.state.cell.y - 1], node.state.ori,
                                         node.state.pok_so_far + output_has_poke, node.state.pok_locations + poks)
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        elif node.state.ori == Direction.Direction.South:
            if not node.state.cell.x + 1 >= maze.grid.__len__():
                if not maze.grid[node.state.cell.x + 1][node.state.cell.y].is_wall:
                    if maze.grid[node.state.cell.x + 1][node.state.cell.y].has_poke:
                        if (node.state.cell.x + 1, node.state.cell.y) not in node.state.pok_locations:
                            output_has_poke = 1
                            poks = node.state.pok_locations + [(node.state.cell.x + 1, node.state.cell.y)]
                            # print("poks: {0}, nodes.pok_locs: {1}".format(poks, node.state.pok_locations))
                    output_state = State(maze.grid[node.state.cell.x + 1][node.state.cell.y], node.state.ori,
                                         node.state.pok_so_far + output_has_poke, node.state.pok_locations + poks)
                    return Node(output_state, node, OperatorType.Move, node.depth + 1, node.path_cost + 1)
                return None
            return None

        print("ERROR")

    @staticmethod
    def turn_right(maze, node):
        if node.state.ori == Direction.Direction.East:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.South,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.North:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.East,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.West:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.North,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.South:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.West,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Right, node.depth + 1, node.path_cost)

    @staticmethod
    def turn_left(maze, node):
        if node.state.ori == Direction.Direction.East:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.North,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.North:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.West,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.West:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.South,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.South:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.East,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Left, node.depth + 1, node.path_cost)

    @staticmethod
    def turn_back(maze, node):
        if node.state.ori == Direction.Direction.East:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.West,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.North:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.South,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.West:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.East,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)

        elif node.state.ori == Direction.Direction.South:
            output_state = State(maze.grid[node.state.cell.x][node.state.cell.y], Direction.Direction.North,
                                 node.state.pok_so_far, node.state.pok_locations)
            return Node(output_state, node, OperatorType.Back, node.depth + 1, node.path_cost)


# 'Test'
# initial_cell = Cell(1, 1, False, False)
# initial_state = State(initial_cell, Direction.North, 0)
# initial_node = Node(initial_state, None, None, 0, 0)
# move(initial_node)
# print(str(initial_cell))