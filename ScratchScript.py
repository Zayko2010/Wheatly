__author__ = 'Sabrout'
from Maze import Maze
from Operator import Operator
from Cell import Cell
from State import State
from Node import Node
from Direction import Direction

search_maze = Maze()
operator = Operator()

print("-------Maze-------")
print("PokeNo: {0}, Hatch Units: {1}".format(search_maze.poke, search_maze.hatch_units))
print("Size = {0}x{1}").format(search_maze.x, search_maze.y)
print("StartCell ({0},{1})".format(search_maze.start_pos[0], search_maze.start_pos[1]))
print("EndCell   ({0},{1})".format(search_maze.end_pos[0], search_maze.end_pos[1]))

initial_cell = Cell(search_maze.x, search_maze.y, False, False)
initial_state = State(initial_cell, Direction.South, 0)
initial_node = Node(initial_state, None, None, 0, 0)

# printing the maze
# print("  "),
# for i in range(search_maze.grid[0].__len__()):
#     print("{0} ").format(i),
# print(" ")
# for i in range(search_maze.maze.__len__()):
#     print(i),
#     print(search_maze.maze[i])

print(" ")
print("-------Grid-------")
print("  "),
for i in range(search_maze.grid[0].__len__()):
    print("{0} ").format(i),
print("Y")
for i in range(search_maze.grid.__len__()):
    print(i),
    print(search_maze.print_grid()[i])
print("X")

print("-------Agent-------")
print("LocBefore ({0},{1})".format(initial_cell.x, initial_cell.y))

next_node = operator.move(search_maze, initial_node)

if not next_node : print("Wall!!")
else : print("LocAfter ({0},{1})".format(next_node.state.cell.x, next_node.state.cell.y))