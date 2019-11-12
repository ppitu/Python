
class Node:
	"""Klasa reprezentujaca wezel listy jednokierunkowej"""

	def __init__(self, data = None, next = None):
		self.data = data
		self.next = next

	def __str__(self):
		return str(self.data) #bardzo ogolnie

class SingleList:
	"""Klasa reprezetujaca liste jednokierunkowa"""

	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None

	def is_empty(self):
		return self.length == 0

	def count(self):	#tworzymy interfejs do odczytu
		return self.length

	def insert_head(self, node):
		if self.length == 0:
			self.head = self.tail = node
		else:
			node.next = self.head
			self.head = node
		self.length += 1

	def insert_tail(self, node):
		if self.length == 0:
			self.head = self.tail = node
		else:
			self.tail.next = node
			self.tail = node
		self.length += 1

	def remove_head(self):
		if self.length == 0:
			raise ValueError("pusta lista")
		node = self.head
		self.head = self.head.next
		node.next = None #Czyszczenie lacza
		self.length -= 1
		if self.length == 0:	#zabezpieczenie
			self.tail = None
		return node	#zwracamy usuniety

	def remove_tail(self):
		if self.length == 0:
			raise ValueError("pusta list")
		if self.head == self.tail:
			return self.remove_head()
		last_one = self.head
		node = self.tail
		while last_one.next != self.tail:
			last_one = last_one.next

		#self.tail.next = None
		self.tail = last_one

		self.length -= 1
		if self.length == 0:
			self.head = None

		return node

	def merge(self, other):
		if other.head == None:
			return 
		
		while other.head != None:
			self.insert_tail(other.head)
			other.head = other.head.next


	def clear(self):
		while self.head != None:
			node = self.head
			self.head = self.head.next
			node.next = None
		self.length = 0
			
