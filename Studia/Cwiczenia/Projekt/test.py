from tree import *
import os

import unittest
import random

class Test(unittest.TestCase):
	myTree = AVLTree()

	def test1_dodania_elementow(self):
		print("Dodanie elementow w kolejnosc rosnacej")
		for x in range(20):
			self.myTree.insert(x)

	def test2_zrownowazone(self):
		print("Test sprawdza czy zrownowazone")
		self.assertTrue(self.myTree.is_avl())

	def test3_dodanie_elementow_odwrotnie(self):
		print("Dodanie elementow w kolejnosc malejacej")
		for x in range(20):
			self.myTree.delete(x)

		for x in range(20):
			self.myTree.insert(20 - x)
	
	def test4_zrownowazone1(self):
		print("Test sprawdza czy zronowazone")
		self.assertTrue(self.myTree.is_avl())
	

	def test5_dodanie_losowych_elementow(self):
		print("Dodanie losowych elementow do drzewa")
		for x in range(20):
			self.myTree.delete(x)

		for x in range(30):
			self.myTree.insert(random.randrange(100))

	def test6_zrownowazone2(self):
		print("Test sprawdza czy zrownowazone")
		self.assertTrue(self.myTree.is_avl())
		

if __name__ == '__main__':
	unittest.main()
