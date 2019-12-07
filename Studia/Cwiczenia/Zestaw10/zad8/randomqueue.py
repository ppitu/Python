import random


class RandomQueue:
	
	def __init__(self):
		self.items = []		

	def insert(self, item):
		self.items.append(item)
	
	def remove(self):
		if self.is_empty():
			raise IndexError

		return self.items.pop(random.randrange(len(self.items)))

	def is_empty(self):
		if len(self.items) == 0:
			return True
		
		return False

	def is_full(self): pass

	def clear(self):
		for x in range(len(self.items)):
			self.items.pop()
