__author__ = 'Sabrout'


class State:
    """Class represents the attributes of a State"""

    def __init__(self, cell, ori, pok_so_far):
        self.cell = cell
        self.ori = ori
        self.pok_so_far = pok_so_far