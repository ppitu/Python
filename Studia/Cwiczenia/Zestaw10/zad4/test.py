from queue import *

import unittest

class Test(unittest.TestCase):
	queue = Queue()

	def test_czy_pusta(self):
		print("Sprawdzenie czy pusta")
		self.assertTrue(self.queue.is_empty())

	def test_czy_pelna(self):
		print("Sprawdzenie czy pelna")
		self.assertFalse(self.queue.is_full())

	def test_dodanie_elementow(self):
		print("Dodanie 5 elementow")
		for i in range(5):
			self.queue.put((i+1)*10)

	def test_dodanie_poza_wielkosc_kolejki(self):
		print("Dodanie poza welkosc kolejki")
		with self.assertRaises(ValueError):
			self.queue.put(1)

	def test_usuwanie_elementow(self):
		print("Usuwanie elementow")
		while not self.queue.is_empty():
			self.queue.get()

if __name__ == '__main__':
	unittest.main()
