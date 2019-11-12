
class Node:
	"""Klasa reprezentuje wezel drzewa binarnego"""
	
	def __init__(self, data = None, left = None, right = None):
		self.data = data
		self.left = left
		self.right = right

	def __str__(self):
		return str(self.data)


def bst_max(top):
	if top == None:
		raise ValueError

	while top.right != None:
		top = top.right

	return top.data

def bst_min(top):
	if top == None:
		raise ValueError
	
	while top.left != None:
		top = top.left

	return top.data

# Ręczne budowanie większego drzewa.
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print('Najwiekszy element: ', bst_max(root))
print('Najmniejszy element: ', bst_min(root))

root1 = None

bst_max(root1)
