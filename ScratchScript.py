__author__ = 'Sabrout'
from Tree import Tree
from Cell import Cell


testTree = Tree()
print(testTree.root.state.cell.__str__())
initialCell = Cell(1, 1, False, False)
# print(str(initialCell))
q = list()
q.append(1)
q.append(2)
q.append(3)
q.append(4)
q.append(5)
q.append(6)
q.append(7)
q.append(8)
q.append(9)
q.append(0)

print(q)

q.remove(1)
q.insert(3, 1)

print(q)