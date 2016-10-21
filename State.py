__author__ = 'Sabrout'


class State:
    """Class represents the attributes of a State"""

    def __init__(self, cell, ori, pok_so_far, pok_locations):
        self.cell = cell
        self.ori = ori
        self.pok_so_far = pok_so_far

        self.pok_locations = pok_locations
