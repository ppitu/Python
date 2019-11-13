
class Queue:
	
	def __init__(self, size = 5):
		self.n = size + 1
		self.items = self.n * [None]
		self.head = 0
		self.tail = 0

	def is_empty(self):
		return self.head == self.tail

	def is_full(self):
		return (self.head + self.n - 1) % self.n == self.tail

	def put(self, data):
		if self.tail + 1 == self.n:
			raise IndexError

		self.items[self.tail] = data
		self.tail = (self.tail + 1) % self.n

	def get(self):
		if self.tail == self.head:
			raise IndexError

		data = self.items[self.head]
		self.items[self.head] = None
		self.head = (self.head + 1) % self.n
		return data
