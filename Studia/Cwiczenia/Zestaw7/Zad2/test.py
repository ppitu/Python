from rectangles import *

import unittest

class TestRectangle(unittest.TestCase):
	def test_wyjatow_konstruktora(self):
		with self.assertRaises(ValueError):
			Rectangle(3, 4, 1, 2)
	
	def test_str_oraz_repr(self):
		self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")
		self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")

	def test_porownanie_oraz_negacja(self):
		self.assertTrue(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4))
		self.assertFalse(Rectangle(1, 2, 3, 4) == Rectangle(3, 4, 5, 6))
		self.assertTrue(Rectangle(1, 2, 3, 4) != Rectangle(3, 4, 5, 6))

	def test_center(self):
		self.assertEqual(Rectangle(1, 2, 4, 5).center(), Point(2.5, 3.5))
		self.assertEqual(Rectangle(4, 4, 5, 5).center(), Point(4.5, 4.5))
	
	def test_pole_powierzchni(self):
		self.assertEqual(Rectangle(0, 2, 3, 4).area(), 6)
		self.assertEqual(Rectangle(2, 2, 4, 4).area(), 4)

	def test_Przesuniecie(self):
		self.assertEqual(Rectangle(1, 2, 3, 4).move(1, 2), Rectangle(2, 4, 4, 6))
		self.assertEqual(Rectangle(1, 2, 4, 6).move(-1, -3), Rectangle(0, -1, 3, 3))

	def test_intersection(self):
		self.assertEqual(Rectangle(2, 2, 4, 4).intersection(Rectangle(3, 3, 5, 5)), Rectangle(3, 3, 4, 4))

	def test_cover(self):
		self.assertEqual(Rectangle(2, 2, 4, 4).cover(Rectangle(4, 5, 5, 5)), Rectangle(2, 2, 5, 5))

	def test_make4(self):
		self.assertEqual(Rectangle(2, 2, 4, 4).make4(), [Rectangle(2, 2, 3, 3), Rectangle(3, 3, 4, 4), Rectangle(2, 3, 3, 4), Rectangle(3, 2, 4, 3)])

if __name__ == '__main__':
	unittest.main()
