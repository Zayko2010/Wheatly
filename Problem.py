from abc import ABCMeta, abstractmethod


class Problem:
    __metaclass__ = ABCMeta

    def __init__(self, initial_state, operators, state_space):
        self.initial_state = initial_state
        self.operators = operators
        self.state_space = state_space

    @abstractmethod
    def goal_test(self, node):
        pass

    @abstractmethod
    def path_cost(self, node):
        pass