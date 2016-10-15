from Maze import Maze
from Operator import Operator

maze = Maze()
operator = Operator()


print("Maze from Search has_poke[0][2]: {0}".format(maze.grid[0][2].has_poke))
operator.move(maze)
print("Maze from Search has_poke[0][2]x2: {0}".format(maze.grid[0][2].has_poke))
# def general_search():
