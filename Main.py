from Maze import Maze
from Operator import Operator
from Tree import Tree
import OperatorType
from GottaCatchEmAll import GottaCatchEmAll
import Problem


def search(maze, strategy):
    if strategy not in ["BF", "DF", "ID", "UC", "GR1", "GR2", "GR3", "AS1", "AS2", "AS3"]:
        print "The search strategy \"{0}\" is not recognized!"
        return None

    if strategy == "BF":
        return breadth_first_search(maze)
    elif strategy == "DF":
        return depth_first_search(maze)
    elif strategy == "ID":
        return iterative_deepening_search(maze)
    elif strategy == "UC":
        return uniform_cost_search(maze)


def breadth_first_search(maze):
    tree = Tree(maze)
    nodes = 0
    while True:
        if not tree.q:
            return [None, None, nodes]

        node = tree.q.pop(0)
        nodes += 1

        if gotta.goal_test(node):
            return [path(node), node.path_cost, nodes]

        tree.q.extend(gotta.expand(node))


def depth_first_search(maze):
    tree = Tree(maze)
    nodes = 0
    while True:
        if not tree.q:
            return [None, None, nodes]

        node = tree.q.pop()
        nodes += 1

        if gotta.goal_test(node):
            return [path(node), node.path_cost, nodes]

        tree.q.extend(gotta.expand(node))


def iterative_deepening_search(maze):
    nodes = 0
    for limit in range(float("inf")):
        goal_node = depth_limited_search(limit, maze)
        if goal_node[0]:
            return goal_node
        else:
            nodes += goal_node[1]


def depth_limited_search(limit, maze):
    tree = Tree(maze)
    nodes = 0
    while True:
        if not tree.q:
            return [None, None, nodes]

        node = tree.q.pop()
        nodes += 1

        if gotta.goal_test(node):
            return [path(node), node.path_cost, nodes]
        if node.depth == limit:
            continue
        else:
            tree.q.extend(gotta.expand(node))


def uniform_cost_search(maze):
    tree = Tree(maze)
    nodes = 0
    while True:
        if not tree.q:
            return [None, None, nodes]

        node = tree.q.pop(0)

        if gotta.goal_test(node):
            return [path(node), node.path_cost, nodes]

        expansion_nodes = gotta.expand(node)
        nodes += 1

        for new_node in expansion_nodes:
            if new_node:
                tree.q.insert(new_node.path_cost, new_node)
                expansion_nodes.remove(new_node)


def path(node):
    nodes = []
    while node:
        nodes += node
        node = node.parent_node

    nodes = nodes.reverse()
    path_str = ""

    for node in nodes:
        path_str += ("[Cell ({0}, {1}), Dir: {2}] \n".format(node.state.cell.x, node.state.cell.y,
                                                             "North" if node.state.ori == 1 else "East"
                                                             if node.state.ori == 2 else
                                                             "South" if node.state.ori == 3 else "West"))


maze_new = Maze()
gotta = GottaCatchEmAll(Operator(), maze_new, Tree(maze_new).root)


# Test Zone

# search_maze = Maze()
# operator = Operator()
#
#
# print(" ")
# print("-------Maze-------")
# print("  "),
# for i in range(search_maze.maze.__len__()):
# print "{0} ".format(i),
# print("Y")
# for i in range(search_maze.maze.__len__()):
#     print(i),
#     print(search_maze.maze[i])
# print("X")
#
# print(" ")
# print("-------Grid-------")
# print("  "),
# for i in range(search_maze.grid[0].__len__()):
#     print "{0} ".format(i),
# print("Y")
# for i in range(search_maze.grid.__len__()):
#     print(i),
#     print(search_maze.print_grid()[i])
# print("X")
#
#
# out = search(search_maze)
#
# print("-------Maze-------")
# print("PokeNo: {0}, Hatch Units: {1}".format(search_maze.poke, search_maze.hatch_units))
# print("StartCell_X = {0}, StartCell_Y = {1}".format(search_maze.start_pos[0], search_maze.start_pos[1]))
# print("EndCell_X = {0}, EndCell_Y = {1}".format(search_maze.end_pos[0], search_maze.end_pos[1]))
#
# if out is None:
#     print("None")
# else:
#     print("-------Solution-------")
#     print("Pokes Collected: {0}, Units Walked: {1}".format(out.state.pok_so_far, out.path_cost))
#     print("AgentCell_X = {0}, AgentCell_Y = {1}".format(out.state.cell.x, out.state.cell.y))
#     print("Path:")
#     node = out
#     while node:
#         print("[({0}, {1}), Dir: {2}]".format(node.state.cell.x, node.state.cell.y, node.state.ori))
#         node = node.parent_node
# print("Before Move in Search: " + str(tree.root.state.cell))
# tree.q.append(operator.move(maze, tree.root))
# tree.q.pop(0)
# print("After Move in Search: " + str(tree.q.pop().state.cell))
# def general_search():
