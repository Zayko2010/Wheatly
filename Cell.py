class Cell:

    def __init__(self, x, y, isWall, hasPoke):
        self.x = x
        self.y = y
        self.isWall = isWall
        self.hasPoke = hasPoke

    def __str__(self):
        return "Cell : " + str(self.x) + ", " + str(self.y)