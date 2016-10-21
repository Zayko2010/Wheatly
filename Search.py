from Maze import Maze
from Operator import Operator
from Tree import Tree
import OperatorType


def search(maze):
    tree = Tree(maze)
    i = 0
    while True:
        # print("------------------------------")
        if not tree.q:
            # print("Not Tree.Q")
            return None
        node = tree.q.pop(0)
        # print("i = {0}".format(i))
        # print("PokeCol: {0}, UntWlk: {1},".format(node.state.pok_so_far, node.path_cost)),
        # print("Ag_X = {0}, Ag_Y = {1}, AgL: {2},".format(node.state.cell.x, node.state.cell.y, node.state.ori)),
        # print("Op = {0}, poks_loc: {1}".format(node.operator_type, node.state.pok_locations))
        if goal_test(node):
            print("i = {0}".format(i))
            return node
        # printQ(tree.q)
        tree.q.extend(expand(node))
        # printQ(tree.q)
        i += 1
        # print("------------------------------")


def goal_test(node):
    if node.state.pok_so_far >= search_maze.poke:
        if node.state.cell.x == search_maze.end_pos[0]:
            if node.state.cell.y == search_maze.end_pos[1]:
                if node.path_cost >= search_maze.hatch_units:
                    return True
    return False


def expand(node):
    nodes = list()
    # print(node.state.pok_locations)
    move_node = operator.move(search_maze, node)
    # print(node.state.pok_locations)
    # print("Move Node {0}".format(bool(move_node)))
    if move_node:
        # print("Move Node {0}".format(move_node.state.cell))
        # print(move_node.state.pok_locations)
        nodes.append(move_node)
    # else:
    #     print("Wall!")
    if node.operator_type == OperatorType.OperatorType.Move or not node.operator_type:
        # print("Rotate Operators")
        nodes.append(operator.turn_back(search_maze, node))
        nodes.append(operator.turn_left(search_maze, node))
        nodes.append(operator.turn_right(search_maze, node))
    # print(not nodes)
    # print(node.state.pok_locations)
    return nodes


def printQ(q):
    print("Node Q : ["),
    for node in q:
        print("PokeCol: {0}, UntWlk: {1},".format(node.state.pok_so_far, node.path_cost)),
        print("Ag_X = {0}, Ag_Y = {1}, AgL: {2},".format(node.state.cell.x, node.state.cell.y, node.state.ori)),
        print("Op = {0} ||".format(node.operator_type)),
    print("]")

#Test Zone

search_maze = Maze()
operator = Operator()


print(" ")
print("-------Maze-------")
print("  "),
for i in range(search_maze.maze.__len__()):
    print "{0} ".format(i),
print("Y")
for i in range(search_maze.maze.__len__()):
    print(i),
    print(search_maze.maze[i])
print("X")

print(" ")
print("-------Grid-------")
print("  "),
for i in range(search_maze.grid[0].__len__()):
    print "{0} ".format(i),
print("Y")
for i in range(search_maze.grid.__len__()):
    print(i),
    print(search_maze.print_grid()[i])
print("X")


out = search(search_maze)

print("-------Maze-------")
print("PokeNo: {0}, Hatch Units: {1}".format(search_maze.poke, search_maze.hatch_units))
print("StartCell_X = {0}, StartCell_Y = {1}".format(search_maze.start_pos[0], search_maze.start_pos[1]))
print("EndCell_X = {0}, EndCell_Y = {1}".format(search_maze.end_pos[0], search_maze.end_pos[1]))

if out is None:
    print("None")
else:
    print("-------Solution-------")
    print("Pokes Collected: {0}, Units Walked: {1}".format(out.state.pok_so_far, out.path_cost))
    print("AgentCell_X = {0}, AgentCell_Y = {1}".format(out.state.cell.x, out.state.cell.y))
    print("Path:")
    node = out
    while node:
        print("[({0}, {1}), Dir: {2}]".format(node.state.cell.x, node.state.cell.y
                                              , "North" if node.state.ori == 1 else "East" if node.state.ori == 2 else
                                              "South" if node.state.ori == 3 else "West"))
        node = node.parent_node
# print("Before Move in Search: " + str(tree.root.state.cell))
# tree.q.append(operator.move(maze, tree.root))
# tree.q.pop(0)
# print("After Move in Search: " + str(tree.q.pop().state.cell))
# def general_search():
