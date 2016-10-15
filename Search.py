from Maze import Maze
from Operator import Operator
from Tree import Tree


maze = Maze()
tree = Tree(maze)
operator = Operator()


print("Before Move in Search: " + str(tree.root.state.cell))
tree.q.append(operator.move(maze, tree.root))
tree.q.pop(0)
print("After Move in Search: " + str(tree.q.pop().state.cell))
# def general_search():
