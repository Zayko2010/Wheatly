from Maze import Maze
from Operator import Operator
from Tree import Tree
import OperatorType


def search(maze):
    tree = Tree(maze)
    i = 0
    while i <= 1000:
        if not tree.q:
            return None
        node = tree.q.pop()
        print("i = {0}".format(i))
        print("Pokes Collected: {0}, Units Walked: {1}".format(node.state.pok_so_far, node.path_cost))
        print("AgentCell_X = {0}, AgentCell_Y = {1}".format(node.state.cell.x, node.state.cell.y))
        if goal_test(node):
            return node
        tree.q.extend(expand(node))
        i += 1


def goal_test(node):
    if node.state.pok_so_far >= search_maze.poke:
        if node.state.cell.x == search_maze.end_pos[0]:
            if node.state.cell.y == search_maze.end_pos[1]:
                if node.path_cost >= search_maze.hatch_units:
                    return True
    return False


def expand(node):
    nodes = list()
    move_node = operator.move(search_maze, node)
    print("Move Node {0}".format(bool(move_node)))
    if bool(move_node):
        print("Move Node detail {0}".format(move_node.state.cell))
        nodes.append(move_node)
    if node.operator_type == OperatorType.OperatorType.Move:
        nodes.append(operator.turn_back(search_maze, node))
        nodes.append(operator.turn_left(search_maze, node))
        nodes.append(operator.turn_right(search_maze, node))
    print(not nodes)
    return nodes


search_maze = Maze()
operator = Operator()
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
# print("Before Move in Search: " + str(tree.root.state.cell))
# tree.q.append(operator.move(maze, tree.root))
# tree.q.pop(0)
# print("After Move in Search: " + str(tree.q.pop().state.cell))
# def general_search():
