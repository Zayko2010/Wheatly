import Problem
from Maze import Maze
from Operator import Operator
from Tree import Tree
import OperatorType


class GottaCatchEmAll(Problem):

    def __init__(self, initial_state, maze, operators):
        self.initial_state = initial_state
        self.maze = maze
        self.operators = operators

    def goal_test(self, node):
        if node.state.pok_so_far >= self.maze.poke:
            if node.state.cell.x == self.maze.end_pos[0]:
                if node.state.cell.y == self.maze.end_pos[1]:
                    if node.path_cost >= self.maze.hatch_units:
                        return True
        return False

    def path_cost(self, node):
        return node.path_cost

    def expand(self, node):
        nodes = list()
        move_node = self.operators.move(self.maze, node)

        if move_node:
            nodes.append(move_node)

        if node.operator_type == OperatorType.OperatorType.Move or not node.operator_type:
            nodes.append(self.operators.turn_back(self.maze, node))
            nodes.append(self.operators.turn_left(self.maze, node))
            nodes.append(self.operators.turn_right(self.maze, node))

        return nodes