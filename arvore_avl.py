# Guilherme Azambuja — 149 429


class Tree:

	def __init__(self):
		self.root: Node

		self.root = None

	def insert(self, info: int):
		newNode: Node
		newRoot: Node
		rootSwap: bool

		if self.root:
			setattr(self.root, 'is_root', True)
			newNode, newRoot = self.root.insert(info)
			rootSwap = not getattr(self.root, 'is_root')
			delattr(self.root, 'is_root')
			if rootSwap:
				self.root = newRoot
			return newNode

		else:
			self.root = Node(info)
			return self.root

	def remove(self, info: int):
		newRoot: Node
		rootSwap: bool

		setattr(self.root, 'is_root', True)
		newRoot = self.root.remove(info)
		rootSwap = not getattr(self.root, 'is_root')
		delattr(self.root, 'is_root')
		if rootSwap:
			self.root = newRoot
		return newRoot

	def search(self, info: int):
		return self.root.search(info)


class Node:

	def __init__(self, info: int):
		self.ls: Node
		self.rs: Node
		self.h: int

		self.info = info
		self.ls = None
		self.rs = None
		self.h = 0

	def __str__(self):
		if self.ls:
			li = str(self.ls.info)
		else:
			li = '--'
		if self.rs:
			ri = str(self.rs.info)
		else:
			ri = '--'
		return f'Info: {self.info}, Height: {self.h}, [{li} | {ri}]'

	def insert(self, info: int):
		newNode: Node
		newRoot: Node

		if info < self.info:
			if self.ls is None:  # Caso base
				self.ls = Node(info)
				self.h = self.getHeight()
				return self.ls, False
			else:  # Caso recursivo
				newNode = self.ls.insert(info)[0]
				if newNode:
					newRoot = self.balance()
					if newRoot:  # Se houve modificação e há uma nova raiz para essa subárvore
						if newRoot.ls:
							newRoot.ls.h = newRoot.ls.getHeight()
						if newRoot.rs:
							newRoot.rs.h = newRoot.rs.getHeight()
						newRoot.h = newRoot.getHeight()
					self.h = self.getHeight()
					return newNode, newRoot
				else:
					return False, False

		elif info > self.info:
			if self.rs is None:
				self.rs = Node(info)
				self.h = self.getHeight()
				return self.rs, False
			else:
				newNode = self.rs.insert(info)[0]
				if newNode:
					newRoot = self.balance()
					if newRoot:
						if newRoot.ls:
							newRoot.ls.h = newRoot.ls.getHeight()
						if newRoot.rs:
							newRoot.rs.h = newRoot.rs.getHeight()
						newRoot.h = newRoot.getHeight()
					self.h = self.getHeight()
					return newNode, newRoot
				else:
					return False, False

		else:
			return False, False  # Info já existe na árvore

	def remove(self, info: int):
		target: Node
		parent: Node
		side: str

		parent, side = self.getParent(info)
		if not parent:
			return None
		target = getattr(parent, side)
		if target.h == 0:  # Nodo a ser apagado é folha
			setattr(parent, side, None)
		return self.balance()

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

	def getParent(self, info: int):
		if self.ls.info == info:
			return self, 'ls'
		elif self.rs.info == info:
			return self, 'rs'
		else:
			if info < self.info:
				if self.ls is not None:
					return self.ls.getParent(info)
				else:
					return None
			else:
				if self.rs is not None:
					return self.rs.getParent(info)
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

			if hasattr(self, 'is_root'):  # Caso a raiz da árvore seja movida
				setattr(self, 'is_root', False)

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

			if hasattr(self, 'is_root'):
				setattr(self, 'is_root', False)

			if rrh >= rlh:
				return self.leftRotate()
			else:
				return self.rightLeftRotate()

		else:
			return False  # Árvore já está balanceada

	def leftRotate(self):
		newRoot: Node
		info: int

		newRoot = self.rs
		self.rs = newRoot.ls
		newRoot.ls = self
		return newRoot

	def rightRotate(self):
		newRoot: Node
		info: int

		newRoot = self.ls
		self.ls = newRoot.rs
		newRoot.rs = self
		return newRoot

	def leftRightRotate(self):
		self.ls = Node.leftRotate(self.ls)
		return self.rightRotate()

	def rightLeftRotate(self):
		self.rs = Node.rightRotate(self.rs)
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
