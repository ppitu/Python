from rectangles import *

import unittest

class TestRectangle(unittest.TestCase):

	def test_str_and_repr(self):
		self.assertEqual(str(Rectangle(1, 2, 3, 4)), "[(1, 2), (3, 4)]")
		self.assertEqual(repr(Rectangle(1, 2, 3, 4)), "Rectangle(1, 2, 3, 4)")

	def test_porownywanie(self):
		self.assertFalse(Rectangle(1, 2, 3, 4) == Rectangle(5, 6, 7, 8))
		self.assertTrue(Rectangle(1, 2, 3, 4) == Rectangle(1, 2, 3, 4))
		self.assertTrue(Rectangle(1, 2, 3, 4) != Rectangle(5, 6, 7, 8))
		self.assertFalse(Rectangle(1, 2, 3, 4) != Rectangle(1, 2, 3, 4))

	def test_srodek(self):
		self.assertEqual(Rectangle(1, 2, 4, 5).center(), Point(2.5, 3.5))
		self.assertEqual(Rectangle(4, 4, 5, 5).center(), Point(4.5, 4.5))

	def test_pole_powierzchni(self):
		self.assertEqual(Rectangle(0, 2, 3, 4).area(), 6)
		self.assertEqual(Rectangle(2, 2, 4, 4).area(), 4)

	def test_Przesuniecie(self):
		self.assertEqual(Rectangle(1, 2, 3, 4).move(1, 2), Rectangle(2, 4, 4, 6))
		self.assertEqual(Rectangle(1, 2, 4, 6).move(-1, -3), Rectangle(0, -1, 3, 3))

if __name__ == '__main__':
	unittest.main()
