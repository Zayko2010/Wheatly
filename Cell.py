class Cell:

    def __init__(self, x, y, is_wall, has_poke):
        self.x = x
        self.y = y
        self.is_wall = is_wall
        self.has_poke = has_poke

    def __str__(self):
        return "Cell : " + str(self.x) + ", " + str(self.y)