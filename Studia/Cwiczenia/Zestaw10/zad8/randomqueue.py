import random


class RandomQueue:
	
	def __init__(self):
		self.items = []		

	def insert(self, item):
		self.items.append(item)
	
	def remove(self):
		if self.is_empty():
			raise ValueError
		zmienna = random.randrange(len(self.items))
		temp = self.items[len(self.items) - 1]
		self.items[len(self.items) - 1] = self.items[zmienna]
		self.items[zmienna] = temp

		return self.items.pop(len(self.items) - 1)


	def is_empty(self):
		if len(self.items) == 0:
			return True
		
		return False

	def is_full(self):
		return True

	def clear(self):
		for x in range(len(self.items)):
			self.items.pop()
