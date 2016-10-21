from Maze import Maze
from Operator import Operator
from Tree import Tree
import OperatorType
from GottaCatchEmAll import GottaCatchEmAll
import Problem


def search(maze, strategy, visualize):
    if strategy not in ["BF", "DF", "ID", "UC", "GR1", "GR2", "GR3", "AS1", "AS2", "AS3"]:
        print "The search strategy \"{0}\" is not recognized!"
        return None

    if strategy == "BF":
        return breadth_first_search(maze, visualize)
    elif strategy == "DF":
        return depth_first_search(maze, visualize)
    elif strategy == "ID":
        return iterative_deepening_search(maze, visualize)
    elif strategy == "UC":
        return uniform_cost_search(maze, visualize)
    elif strategy == "GR1":
        return greedy_search(maze, 1)
    elif strategy == "GR2":
        return greedy_search(maze, 2)
    elif strategy == "GR3":
        return greedy_search(maze, 3)
    elif strategy == "AS1":
        return a_star_search(maze, 1)
    elif strategy == "AS2":
        return a_star_search(maze, 2)
    elif strategy == "AS3":
        return a_star_search(maze, 3)


def breadth_first_search(maze, visualize):
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

        if visualize:
            print("ColPoke: {0}, UntWlk: {1},".format(node.state.pok_so_far, node.path_cost)),
            print("Ag_X = {0}, Ag_Y = {1}, AgL: {2},".format(node.state.cell.x, node.state.cell.y, node.state.ori)),
            print("Op = {0}, poks_loc: {1}".format(node.operator_type, node.state.pok_locations))
            print("--------------------------------------------")


def depth_first_search(maze, visualize):
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

        if visualize:
            print("ColPoke: {0}, UntWlk: {1},".format(node.state.pok_so_far, node.path_cost)),
            print("Ag_X = {0}, Ag_Y = {1}, AgL: {2},".format(node.state.cell.x, node.state.cell.y, node.state.ori)),
            print("Op = {0}, poks_loc: {1}".format(node.operator_type, node.state.pok_locations))
            print("--------------------------------------------")


def iterative_deepening_search(maze, visualize):
    nodes = 0
    limit = 0
    while True:
        if visualize:
            print "--------------- NEW LIMIT = {0} ------------------".format(limit)
        goal_node = depth_limited_search(limit, maze, visualize)
        if goal_node[0]:
            return goal_node
        else:
            nodes += goal_node[2]
        limit += 1


def depth_limited_search(limit, maze, visualize):
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

        if visualize:
            print("ColPoke: {0}, UntWlk: {1},".format(node.state.pok_so_far, node.path_cost)),
            print("Ag_X = {0}, Ag_Y = {1}, AgL: {2},".format(node.state.cell.x, node.state.cell.y, node.state.ori)),
            print("Op = {0}, poks_loc: {1}".format(node.operator_type, node.state.pok_locations))
            print("--------------------------------------------")


def uniform_cost_search(maze, visualize):
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
                # expansion_nodes.remove(new_node)

        if visualize:
            print("ColPoke: {0}, UntWlk: {1},".format(node.state.pok_so_far, node.path_cost)),
            print("Ag_X = {0}, Ag_Y = {1}, AgL: {2},".format(node.state.cell.x, node.state.cell.y, node.state.ori)),
            print("Op = {0}, poks_loc: {1}".format(node.operator_type, node.state.pok_locations))
            print("--------------------------------------------")

def greedy_search(maze, h):
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

        if h == 1:
            h_cost = heuristic_1(node)
        elif h == 2:
            h_cost = heuristic_2(node)
        else:
            h_cost = heuristic_3(node)

        for new_node in expansion_nodes:
            if new_node:
                tree.q.insert(h_cost, new_node)
                # expansion_nodes.remove(new_node)


def a_star_search(maze, h):
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

        if h == 1:
            h_cost = heuristic_1(node)
        elif h == 2:
            h_cost = heuristic_2(node)
        else:
            h_cost = heuristic_3(node)

        for new_node in expansion_nodes:
            if new_node:
                tree.q.insert(new_node.path_cost + h_cost, new_node)
                expansion_nodes.remove(new_node)


def heuristic_1(node):
    return max((gotta.maze.hatch_units - node.path_cost), 0)


def heuristic_2(node):
    current_x = node.state.cell.x
    current_y = node.state.cell.y

    end_x = gotta.maze.end_pos[0]
    end_y = gotta.maze.end_pos[1]

    return min(abs(end_x - current_x), abs(end_y - current_y))


def heuristic_3(node):
    return 0


def path(node):
    nodes = list()
    while node:
        nodes.append(node)
        node = node.parent_node

    nodes.reverse()
    path_str = ""

    for node in nodes:
        path_str += ("[Cell ({0}, {1}), Dir: {2}], ".format(node.state.cell.x, node.state.cell.y,
                                                             "North" if node.state.ori == 1 else "East"
                                                             if node.state.ori == 2 else
                                                             "South" if node.state.ori == 3 else "West"))
    return path_str


maze_new = Maze()
gotta = GottaCatchEmAll(Tree(maze_new).root, maze_new, Operator())

print(" ")
print("-------Grid-------")
print("  "),
for i in range(maze_new.grid[0].__len__()):
    print "{0} ".format(i),
print("Y")
for i in range(maze_new.grid.__len__()):
    print(i),
    print(maze_new.print_grid()[i])
print("X")
print(" ")

# print search(maze_new, "BF", False)
# print search(maze_new, "DF", False)
# print search(maze_new, "ID", False)
# print search(maze_new, "UC", True)
# print search(maze_new, "GR1", False)
# print search(maze_new, "GR2", False)