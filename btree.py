import math

class BTreeNode:
	def __init__(self, leaf = False):
		self.leaf = leaf
		self.keys = []
		self.child = []
  
		self.highlight = False

class BTree:
	def __init__(self, t):
		self.root = BTreeNode(True)

		# Ordem da B-Tree (máximo de filhos)
		self.t = t

		# Limites de chaves
		self.max_keys = self.t - 1
		self.min_children = math.ceil(self.t / 2)
		self.min_keys = self.min_children - 1
  
		self.logs = []

	def log(self, mensagem):
		self.logs.append(mensagem)

	def limpar_logs(self):
		self.logs.clear()

	def limpar_destaques(self):

		def visitar(no):
			no.highlight = False

			for filho in no.child:
				visitar(filho)

		visitar(self.root)
  
	def destacar(self, no):
		if no is not None:
			no.highlight = True
  
	def print_tree(self, x, l = 0):
		print("Level ", l, " ", len(x.keys), end = ":")
		for i in x.keys:
			print(i, end=" ")
		print()
		l += 1
		if len(x.child) > 0:
			for i in x.child:
				self.print_tree(i, l)
	

	def search(self, k, x = None):
		"""Search for key 'k' at position 'x'.
		If 'x' is not specified, then search occurs from root.

		Returns 'None' if 'k' is not found.
		Otherwise returns a tuple of node and index at which the key was found.

		Arguments:
			k -- key to be searched
			x -- position to search from
		"""
		if x != None:
			i = 0
			while i < len(x.keys) and k > x.keys[i]:
				i += 1
			if i < len(x.keys) and k == x.keys[i]:
				return (x, i)
			elif x.leaf:
				return None
			else:
				#Search in children
				return self.search(k, x.child[i])
		else:
			#Search entire tree as node not provided
			return self.search(k, self.root)

	def _insert(self, x, k):
		self.destacar(x)
		i = 0

		while i < len(x.keys) and k > x.keys[i]:
			i += 1

		if x.leaf:

			self.log(f"Nó folha encontrado.")
			self.log(f"Inserindo a chave {k}.")

			x.keys.insert(i, k)

		else:

			self.log(f"Descendo para o filho {i}.")

			self._insert(x.child[i], k)

			if len(x.child[i].keys) > self.max_keys:

				self.log("O filho excedeu o número máximo de chaves.")
				self.log("Realizando divisão.")

				self._split_child(x, i)
    
	def insert(self, k):
		self.limpar_destaques()
		self.limpar_logs()
		self.log(f"Iniciando inserção da chave {k}.")

		self._insert(self.root, k)

		if len(self.root.keys) > self.max_keys:

			self.log("A raiz excedeu o número máximo de chaves.")
			self.log("Criando uma nova raiz.")

			old_root = self.root

			self.root = BTreeNode(False)

			self.root.child.append(old_root)

			self._split_child(self.root, 0)

		self.log("Inserção concluída.")
   
	def _insert_nonfull(self, x, k):
		"""Insert key 'k' at position 'x' in a non-full node

		Arguments:
			x -- Position of node
			k -- key to be inserted
		"""
		i = len(x.keys) - 1
		if x.leaf:
			x.keys.append((None))
			while i >= 0 and k < x.keys[i]:
				x.keys[i + 1] = x.keys[i]
				i -= 1
			x.keys[i + 1] = k
		else:
			while i >= 0 and k < x.keys[i]:
				i -= 1
			i += 1
			if len(x.child[i].keys) == self.max_keys:
				self._split_child(x, i)
				if k > x.keys[i]:
					i += 1
			self._insert_nonfull(x.child[i], k)

	def _split_child(self, x, i):

		y = x.child[i]

		z = BTreeNode(y.leaf)
  
		self.destacar(x)
		self.destacar(y)

		middle = len(y.keys) // 2

		self.log(
			f"Dividindo o nó {y.keys}."
		)

		self.log(
			f"A chave {y.keys[middle]} será promovida."
		)

		x.keys.insert(i, y.keys[middle])

		x.child.insert(i + 1, z)
		self.destacar(z)

		z.keys = y.keys[middle + 1:]

		y.keys = y.keys[:middle]

		if not y.leaf:

			z.child = y.child[middle + 1:]

			y.child = y.child[:middle + 1]

		self.log(
			f"Nó esquerdo: {y.keys}"
		)

		self.log(
			f"Nó direito: {z.keys}"
		)

	def delete(self, x, k):
		self.destacar(x)
		
		if x == self.root:
			self.limpar_destaques()
			self.limpar_logs()

			self.log(f"Iniciando remoção da chave {k}.")

		i = 0

		while i < len(x.keys) and k > x.keys[i]:
			i += 1

		if i < len(x.keys) and x.keys[i] == k:

			self.log(f"Chave {k} encontrada.")

			if x.leaf:

				self.log("A chave está em uma folha.")
				self.log("Removendo diretamente.")

				x.keys.pop(i)

			else:

				self.log("A chave está em um nó interno.")

				self._delete_internal_node(x, i)

			return

		if x.leaf:

			self.log("A chave não foi encontrada.")

			return

		self.log(f"Descendo para o filho {i}.")

		if len(x.child[i].keys) == self.min_keys:

			self.log("O filho possui o número mínimo de chaves.")
			self.log("Será necessário rebalancear.")

			self._fix_child(x, i)

		if i >= len(x.child):
			i = len(x.child)-1

		self.delete(x.child[i], k)

	def _fix_child(self, x, i):

		if i > 0 and len(x.child[i-1].keys) > self.min_keys:

			self.log("Emprestando chave do irmão esquerdo.")

			self._borrow_from_left(x, i)

		elif i < len(x.child)-1 and len(x.child[i+1].keys) > self.min_keys:

			self.log("Emprestando chave do irmão direito.")

			self._borrow_from_right(x, i)

		else:

			self.log("Nenhum irmão pode emprestar.")
			self.log("Realizando fusão.")

			if i < len(x.child)-1:
				self._merge(x, i)
			else:
				self._merge(x, i-1)

	def _delete_internal_node(self, x, i):

		key = x.keys[i]

		left = x.child[i]

		right = x.child[i+1]

		if len(left.keys) > self.min_keys:

			self.log(
				"Substituindo pela predecessora."
			)

			pred = self._get_predecessor(left)

			x.keys[i] = pred

			self.delete(left, pred)

		elif len(right.keys) > self.min_keys:

			self.log(
				"Substituindo pela sucessora."
			)

			succ = self._get_successor(right)

			x.keys[i] = succ

			self.delete(right, succ)

		else:

			self.log(
				"Fundindo os dois filhos."
			)

			self._merge(x, i)

			self.delete(left, key)

	def _get_predecessor(self, x):

		self.log("Buscando a predecessora.")

		while not x.leaf:
			x = x.child[-1]

		self.log(f"Predecessora encontrada: {x.keys[-1]}.")

		return x.keys[-1]
	
	def _get_successor(self, x):

		self.log("Buscando a sucessora.")

		while not x.leaf:
			x = x.child[0]

		self.log(f"Sucessora encontrada: {x.keys[0]}.")

		return x.keys[0]
	
	def _borrow_from_left(self, x, i):
		self.log("Empréstimo do irmão esquerdo.")
		self.destacar(x)
		self.destacar(x.child[i])
		self.destacar(x.child[i-1])
  
		child = x.child[i]
		left = x.child[i-1]
	
	
		child.keys.insert(
			0,
			x.keys[i-1]
		)
	
	
		x.keys[i-1] = left.keys.pop()
	
	
		if not left.leaf:
		
			child.child.insert(
				0,
				left.child.pop()
			)
	
	def _borrow_from_right(self, x, i):
		self.log("Empréstimo do irmão direito.")

		self.destacar(x)
		self.destacar(x.child[i])
		self.destacar(x.child[i+1])
		
		child = x.child[i]
		right = x.child[i+1]
	
	
		child.keys.append(
			x.keys[i]
		)
	
	
		x.keys[i] = right.keys.pop(0)
	
	
		if not right.leaf:
		
			child.child.append(
				right.child.pop(0)
			)
	
	def _merge(self, x, i):
		self.log("Fundindo dois nós.")
  
		left = x.child[i]
		right = x.child[i+1]
		
		self.destacar(x)
		self.destacar(left)
		self.destacar(right)	
	
		# coloca chave do pai no meio
		left.keys.append(
			x.keys.pop(i)
		)
	
	
		# copia chaves do irmão direito
		left.keys.extend(
			right.keys
		)
	
	
		# copia filhos
		if not right.leaf:
		
			left.child.extend(
				right.child
			)
	
	
		# remove irmão direito
		x.child.pop(i+1)
	
	
		# caso a raiz fique vazia
		if x == self.root and len(x.keys) == 0:
			self.log("A raiz ficou vazia.")
			self.log("Promovendo o filho como nova raiz.")
			
			self.root = left