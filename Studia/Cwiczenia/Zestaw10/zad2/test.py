from stack import *
import unittest

class Test(unittest.TestCase):
	stack = Stack()

	def test_dodanie_elementow(self):
		print("Wypelnienie stosu")
		for i in range(10):
			self.stack.push(i)

		print("Sprawdzenie czy pelny")
		self.assertEqual(self.stack.is_full(), True)

	def test_przepelnienia_stosu(self):
		print("Test przepelnienia stosu")
		with self.assertRaises(ValueError):
			self.stack.push(1)

	def test_usuwania_elementow(self):
		print("Usuwanie elementow")
		while not self.stack.is_empty():
			self.stack.pop()
		self.assertEqual(self.stack.is_empty(), True)

if __name__ == '__main__':
	unittest.main()
