from points import *

import unittest

class TestPoints(unittest.TestCase):

	def test_str(self):
		self.assertEqual(str(Point(1, 0)), "(1, 0)")
		self.assertEqual(str(Point(-1, 0)), "(-1, 0)")
		self.assertEqual(repr(Point(1, 0)), "Point(1, 0)")
		self.assertEqual(repr(Point(-1, 0)), "Point(-1, 0)")

	def test_porownanie(self):
		self.assertTrue(Point(1, 0) == Point(1, 0))
		self.assertFalse(Point(1, 0) == Point(1, 2))
		self.assertTrue(Point(1, 0) != Point(1, 2))
		self.assertFalse(Point(1, 0) != Point(1, 0))
	
	def test_dodwanie_wektorow(self):
		self.assertEqual(Point(2, 0) + Point(3, 4), (5, 4))	
		self.assertEqual(Point(-3, 2) + Point(5, 19), (2, 21))

	def test_odejmowanie_wektorow(self):
		self.assertEqual(Point(2, 0) - Point(3, 4), (-1, -4))
		self.assertEqual(Point(4, 5) - Point(1, 1), (3, 4))

	def test_iloczyn_skalarny(self):
		self.assertEqual(Point(2, 0)*Point(3, 4), 6)
		self.assertEqual(Point(2, 6)*Point(3, 1), 12)

	def test_iloczyn_wektorowy(self):
		self.assertEqual(Point(2, 0).cross(Point(3, 4)), 8)
		self.assertEqual(Point(4, 5).cross(Point(2, 6)), 14)
	
	def test_dlugosc(self):
		self.assertEqual(Point(0, 2).length(), 2)
		self.assertEqual(Point(3, 4).length(), 5)

if __name__ == '__main__':
	unittest.main()
