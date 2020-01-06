from randomqueue import *
from random import *
import os

import unittest

class Test(unittest.TestCase):
	queue = RandomQueue()

	def test_wypelnienie_kolejki(self):
		for x in range(10):
			self.queue.insert(x)

	def test_sprawdzenie_czy_pelna(self):
		self.assertTrue(self.queue.is_full())

	def test_usuwanie_elementow(self):
		while not self.queue.is_empty():
			self.queue.remove()

	def test_sprawdzenie_czy_mozna_usunac_z_pustej(self):
		with self.assertRaises(ValueError):
			self.queue.remove()

if __name__ == '__main__':
	unittest.main()
