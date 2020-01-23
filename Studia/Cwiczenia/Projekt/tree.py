
class Node:
	"""Klasa reprezentuje wezel drzewa AVL"""
	
	def __init__(self, data):
		self.data = data	#dane w wezle
		self.left = None	#lewe poddrzewo
		self.right = None	#prawe poddrzewo
		self.height = 1		#wysokosc
		



class AVLTree:
	"""Klasa reprezentujaca drzewo AVL"""
	def __init__(self):
		self.root = None
	

	def insert(self, data):
		self.root = self.insertNode(self.root, data)

	#Dodanie elementu do drzewa
	def insertNode(self, root, data):
		
		#Dodajemy jak to zwyklego drzewa BST
		if not root:
			return Node(data)
		elif data < root.data:
			root.left = self.insertNode(root.left, data)
		else:
			root.right = self.insertNode(root.right, data)
		
		#Uaktualnienie wysokosci dodanego wezla
		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))
		
		#Pobieramy roznice pomiedzy prawym a lewym poddrzewem
		balance = self.getBalance(root)

		#Jezeli nie jest zbalansowane to jest balansujemy
		if balance > 1 and data < root.left.data:
			return self.rightRotate(root)
	
		if balance < -1 and data > root.right.data:
			return self.leftRotate(root)
		
		if balance > 1 and data > root.left.data:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)
		
		if balance < -1 and data < root.right.data:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root)

		return root

	def delete(self, data):
		self.root = self.deleteNode(self.root, data)

	#Usuwanie elementu z drzew
	def deleteNode(self, root, data):
		
		if not root:
			return root

		elif data < root.data:
			root.left = self.deleteNode(root.left, data)
		
		elif data > root.data:
			root.right = self.deleteNode(root.right, data)
		else:
			if root.left is None:
				temp = root.right
				root = None
				return temp
			elif root.right is None:
				temp = root.left
				root = None
				return temp

			temp = self.getMinValueNode(root.right)
			root.data = temp.data
			root.right = self.deleteNode(root.right, temp.data)

		if root is None:
			return root

		root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right))

		balance = self.getBalance(root)

		if balance > 1 and self.getBalance(root.left) >= 0:
			return self.rightRotate(root)

		if balance < -1 and self.getBalance(root.right) <= 0:
			return self.leftRotate(root)

		if balance > 1 and self.getBalance(root.left) < 0:
			root.left = self.leftRotate(root.left)
			return self.rightRotate(root)
		if balance < -1 and self.getBalance(root.right) > 0:
			root.right = self.rightRotate(root.right)
			return self.leftRotate(root) 

		return root
				

	def leftRotate(self, z):
		
		y = z.right
		T2 = y.left

		y.left = z
		z.right = T2

		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))

		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y

	def rightRotate(self, z):
		
		y = z.left
		T3 = y.right

		y.right = z
		z.left = T3

		z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
		
		y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

		return y

	def getHeight(self, root):
		if not root:
			return 0

		return root.height

	def getBalance(self, root):
		if not root:
			return 0
		return self.getHeight(root.left) - self.getHeight(root.right)

	def getMinValueNode(self, root):
		if root is None or root.left is None:
			return root
		
		return self.getMinValueNode(root.left)

	def preOrder(self):
		self.preOrder1(self.root)


	def preOrder1(self, root):
		if not root:
			return

		print("{0} ".format(root.data))
		self.preOrder1(root.left)
		self.preOrder1(root.right)




myTree = AVLTree() 
  
myTree.insert(10) 
myTree.insert(20) 
myTree.insert(30) 
myTree.insert(40) 
myTree.insert(50) 
myTree.insert(25) 

myTree.preOrder() 
print("\n")
myTree.delete(50)
myTree.delete(20)
myTree.preOrder()
