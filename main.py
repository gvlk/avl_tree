from arvore_avl import Tree


arv = Tree()
nodos = list()

nodos.append(arv.insert(50))
nodos.append(arv.insert(60))
nodos.append(arv.insert(40))
nodos.append(arv.insert(45))
nodos.append(arv.insert(55))
nodos.append(arv.insert(30))
nodos.append(arv.insert(10))

print(f"Root: {arv.root}")

for n in nodos:
	print(n)

print()

arv.remove(55)
print(f"Root: {arv.root}")

for n in nodos:
	print(n)

