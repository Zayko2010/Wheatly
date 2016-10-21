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

initial_cell = Cell(search_maze.start_pos[0], search_maze.start_pos[1], False, False)
initial_state = State(initial_cell, Direction.East, 0)
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
# State 1
print("State #1")
print("LocBefore ({0},{1})".format(initial_cell.x, initial_cell.y))
state_one = operator.move(search_maze, initial_node)
pass_on = True
if not state_one :
    print("Wall!!")
    pass_on = False
else :
    print("LocAfter ({0},{1})".format(state_one.state.cell.x, state_one.state.cell.y))
    print("PokemonsSoFar: {0}").format(state_one.state.pok_so_far)

print("-------------------")
# State 2
if pass_on:
    print("State #2")
    print("LocBefore ({0},{1})".format(state_one.state.cell.x, state_one.state.cell.y))
    state_two = operator.move(search_maze, state_one)
    if not state_two : print("Wall!!")
    else :
        print("LocAfter ({0},{1})".format(state_two.state.cell.x, state_two.state.cell.y))
        print("PokemonsSoFar: {0}").format(state_two.state.pok_so_far)