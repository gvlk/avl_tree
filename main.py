from arvore_avl import Tree
from random import randint


arv = Tree(1)
nodos = list()
nodos.append(arv)
c = int()

# while c < 6:
# 	x = randint(10, 99)
# 	nodo = arv.insert(x)
# 	if nodo:
# 		nodos.append(nodo)
# 		c += 1
#
# for n in nodos:
# 	print(n)
#
# print()

nodos.append(arv.insert(3))
nodos.append(arv.insert(4))
nodos.append(arv.insert(9))


nodos.sort(reverse=True, key=lambda tree: tree.h)
for n in nodos:
	print(n)
