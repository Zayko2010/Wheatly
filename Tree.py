from State import State
from Direction import Direction
from Node import Node
import random


class Tree:
    """The class creates the queue of the nodes"""

    def __init__(self, maze):
        initial_cell = maze.grid[maze.start_pos[0]][maze.start_pos[1]]

        'Randomizing Initial Orientation'
        initial_ori = None
        random_ori = random.randint(1, 4)
        if random_ori == 1:
            initial_ori = Direction.North
        if random_ori == 2:
            initial_ori = Direction.East
        if random_ori == 3:
            initial_ori = Direction.South
        if random_ori == 4:
            initial_ori = Direction.West

        initial_state = State(initial_cell, initial_ori, 0, [(-1, -1)])
        self.root = Node(initial_state, None, None, 0, 0)
        self.q = list()
        self.q.append(self.root)