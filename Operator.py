import Direction
from State import State
from Cell import Cell
from enum import Enum
__author__ = 'Sabrout'


class Operator(Enum):
    """Class defines the operators to apply on the states"""

    Move = 1
    Right = 2
    Left = 3
    Back = 4

    @staticmethod
    def move(state):
        if state.ori == Direction.Direction.East:
            state.cell.x += 1
        elif state.ori == Direction.Direction.North:
            state.cell.y += 1
        elif state.ori == Direction.Direction.West:
            state.cell.x -= 1
        elif state.ori == Direction.Direction.South:
            state.cell.y -= 1

    @staticmethod
    def turn_right(state):
        if state.ori == Direction.Direction.East:
            state.ori = Direction.Direction.South
        elif state.ori == Direction.Direction.North:
            state.ori = Direction.Direction.East
        elif state.ori == Direction.Direction.West:
            state.ori = Direction.Direction.North
        elif state.ori == Direction.Direction.South:
            state.ori = Direction.Direction.West

    @staticmethod
    def turn_left(state):
        if state.ori == Direction.Direction.East:
            state.ori = Direction.Direction.North
        elif state.ori == Direction.Direction.North:
            state.ori = Direction.Direction.West
        elif state.ori == Direction.Direction.West:
            state.ori = Direction.Direction.South
        elif state.ori == Direction.Direction.South:
            state.ori = Direction.Direction.East

    @staticmethod
    def turn_back(state):
        if state.ori == Direction.Direction.East:
            state.ori = Direction.Direction.West
        elif state.ori == Direction.Direction.North:
            state.ori = Direction.Direction.South
        elif state.ori == Direction.Direction.West:
            state.ori = Direction.Direction.East
        elif state.ori == Direction.Direction.South:
            state.ori = Direction.Direction.North


'Test'
initialCell = Cell(1, 1, False, False)
initialState = State(initialCell, Direction.Direction.North, 0)
Operator.move(initialState)
print(str(initialCell))