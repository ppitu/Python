from fracs import *

import unittest

class TestFractions(unittest.TestCase):
	def setUp(self):
		self.zero = [0, 1]

	def test_add_frac(self):
		self.assertEqual(add_frac([1, 2], [1, 3]), [5, 6])
		self.assertEqual(add_frac([1, 2], [2, 3]), [7, 6])
		self.assertEqual(add_frac([0, 2], [2, 3]), [2, 3])

	def test_sub_frac(self):
		self.assertEqual(sub_frac([1, 2], [2, 3]), [-1, 6])
		self.assertEqual(sub_frac([1, 2], [-1, 2]), [1, 1])
		self.assertEqual(sub_frac([-1, 2], [2, 3]), [-7, 6])		

	def test_mul_frac(self):
		self.assertEqual(mul_frac([1, 2], [-1, 3]), [-1, 6])
		self.assertEqual(mul_frac([0, 2], [-1, 2]), [0, 1])

	def test_div_frac(self):
		self.assertEqual(div_frac([1, 2], [2, 3]), [3, 4])
		self.assertEqual(div_frac([0, 2], [-1, 2]), [0, 1])

	def test_is_positive(self):
		self.assertEqual(is_positive([1, 2]), True)
		self.assertEqual(is_positive([-1, 2]), False)

	def test_cmp_frac(self):
		self.assertEqual(cmp_frac([1, 4], [2, 4]), -1)
		self.assertEqual(cmp_frac([1, 2], [1, 2]), 0)
		self.assertEqual(cmp_frac([2, 4], [1, 4]), 1)

	def test_frac2float(self):
		self.assertEqual(frac2float([1, 2]), 0.5)
		self.assertEqual(frac2float([2, 2]), 1)

if __name__ == '__main__':
	unittest.main()
