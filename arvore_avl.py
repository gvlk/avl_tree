# Guilherme Azambuja — 149 429


class Tree:

	def __init__(self, info: int):
		self.ls: Tree
		self.rs: Tree
		self.h: int

		self.info = info
		self.ls = None
		self.rs = None
		self.h = 0

	def __str__(self):
		return f'Info: {self.info}, Height: {self.h}'

	def insert(self, info: int):
		newNode: Tree
		newRoot: Tree

		if info < self.info:
			if self.ls is None:  # Caso base
				self.ls = Tree(info)
				self.h = self.getHeight()
				return self.ls
			else:  # Caso recursivo
				newNode = self.ls.insert(info)  # A função retorna uma tupla caso haja rotação
				if isinstance(newNode, tuple):
					self.ls = newNode[1]  # newNode[1] é a nova raiz da sub-árvore
					self.ls.ls.h = self.ls.ls.getHeight()
					self.ls.h = self.ls.getHeight()
					newNode = newNode[0]
				if newNode:
					newRoot = self.balance()
					if newRoot:
						self.h = self.getHeight()
						return newNode, newRoot
					self.h = self.getHeight()
					return newNode
				else:
					return False

		elif info > self.info:
			if self.rs is None:
				self.rs = Tree(info)
				self.h = self.getHeight()
				return self.rs
			else:
				newNode = self.rs.insert(info)
				if isinstance(newNode, tuple):
					self.rs = newNode[1]
					self.rs.rs.h = self.rs.rs.getHeight()
					self.rs.h = self.rs.getHeight()
					newNode = newNode[0]
				if newNode:
					newRoot = self.balance()
					if newRoot:
						self.h = self.getHeight()
						return newNode, newRoot
					self.h = self.getHeight()
					return newNode
				else:
					return False

		else:
			return False  # Info já existe na árvore

	def remove(self, info: int):
		target = self.search(info)
		if target is not None:
			pass
		else:
			return None

	def search(self, info: int):
		if info == self.info:
			return self
		else:
			if info < self.info:
				if self.ls is not None:
					return self.ls.search(info)
				else:
					return None
			else:
				if self.rs is not None:
					return self.rs.search(info)
				else:
					return None

	def getBalance(self) -> int:
		lh: int
		rh: int
		if self.ls is None:
			lh = -1
		else:
			lh = self.ls.h
		if self.rs is None:
			rh = -1
		else:
			rh = self.rs.h
		return lh - rh

	def isBalanced(self) -> bool:
		return abs(self.getBalance()) <= 1

	def balance(self):
		k: int
		llh: int
		lrh: int
		rlh: int
		rrh: int

		k = self.getBalance()
		if k == 2:  # Sub-árvore esquerda é maior
			if self.ls.ls is None:
				llh = -1
			else:
				llh = self.ls.ls.h
			if self.ls.rs is None:
				lrh = -1
			else:
				lrh = self.ls.rs.h

			if llh >= lrh:
				return self.rightRotate()
			else:
				return self.leftRightRotate()

		elif k == -2:  # Sub-árvore direita é maior
			if self.rs.ls is None:
				rlh = -1
			else:
				rlh = self.rs.ls.h
			if self.rs.rs is None:
				rrh = -1
			else:
				rrh = self.rs.rs.h

			if rrh >= rlh:
				self.h -= 2
				return self.leftRotate()
			else:
				return self.rightLeftRotate()

		else:
			return False  # Árvore já está balanceada

	def leftRotate(self):
		newRoot: Tree

		newRoot = self.rs
		self.rs = newRoot.ls
		newRoot.ls = self
		return newRoot

	def rightRotate(self):
		newRoot: Tree

		newRoot = self.ls
		self.ls = newRoot.rs
		newRoot.rs = self
		return newRoot

	def leftRightRotate(self):
		self.ls = Tree.leftRotate(self.ls)
		return self.rightRotate()

	def rightLeftRotate(self):
		self.rs = Tree.rightRotate(self.rs)
		return self.leftRotate()

	def getHeight(self) -> int:
		lh: int
		rh: int

		if self.ls is None:
			lh = -1
		else:
			lh = self.ls.h
		if self.rs is None:
			rh = -1
		else:
			rh = self.rs.h
		return 1 + max(lh, rh)


teste = Tree(1329)
nodo9427 = teste.insert(9427)
nodo3824 = teste.insert(3824)
print()
