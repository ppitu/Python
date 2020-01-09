
class Node:
	"""Klasa reprezentuje wezel drzewa AVL"""
	
	def __init__(self, data):
		self.data = data	#dane w wezle
		self.left = None	#lewe poddrzewo
		self.right = None	#prawe poddrzewo
		self.height = 1		#wysokosc
		



class AVLTree:
	"""Klasa reprezentujaca drzewo AVL"""
	
	#Dodanie elementu do drzewa
	def insert(self, root, data):
		
		#Dodajemy jak to zwyklego drzewa BST
		if not root:
			return Node(data)
		elif data < root.data:
			root.left = self.insert(root.left, data)
		else:
			root.right = self.insert(root.right, data)
		
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

	#Usuwanie elementu z drzew
	def delete(self, root, data):
		
		if not root:
			return root

		elif data < root.data:
			root.left = self.delete(root.left, data)
		
		elif data > root.data:
			root.right = self.delete(root.right, data)
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
			root.right = self.delete(root.right, temp.data)

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


	def preOrder(self, root):
		if not root:
			return

		print("{0} ".format(root.data))
		self.preOrder(root.left)
		self.preOrder(root.right)




myTree = AVLTree() 
root = None
  
root = myTree.insert(root, 10) 
root = myTree.insert(root, 20) 
root = myTree.insert(root, 30) 
root = myTree.insert(root, 40) 
root = myTree.insert(root, 50) 
root = myTree.insert(root, 25) 

myTree.preOrder(root) 
print("\n\n\n")
root = myTree.delete(root, 50)
root = myTree.delete(root, 20)
myTree.preOrder(root)
