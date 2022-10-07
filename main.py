from arvore_avl import Tree
from random import randint


arv = Tree()
numeros_usados = set()
nodos = list()

while True:
	x = randint(1, 9999)
	numeros_usados.add(x)
	nodo = arv.insert(x)
	nodos.append(nodo)
	if nodo:
		if arv.root.h == 5:
			break


print(arv)
for n in nodos:
	print(n)

print()

print(arv)
nodos.sort(reverse=True, key=lambda tree: tree.h)
for n in nodos:
	print(n)
