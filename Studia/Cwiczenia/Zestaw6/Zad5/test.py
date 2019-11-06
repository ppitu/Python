from fracs import *

import unittest

class TestFrac(unittest.TestCase):
	
	def test_wypisywania(self):
		self.assertEqual(str(Frac(1, 2)), '1/2')
		self.assertEqual(repr(Frac(1, 2)), 'Frac(1, 2)')
		self.assertEqual(str(Frac(3, 1)), '3') 

	def test_dodawanie(self):
		self.assertEqual(Frac(1, 2) + Frac(2, 3), Frac(7, 6))
		self.assertEqual(Frac(0, 3) + Frac(3, 4), Frac(3, 4))

	def test_odejmowanie(self):
		self.assertEqual(Frac(1, 2) - Frac(3, 4), Frac(-1, 4))
		self.assertEqual(Frac(0, 3) - Frac(2, 9), Frac(-2, 9))

	def test_mnozenie(self):
		self.assertEqual(Frac(1, 2) * Frac(3, 4), Frac(3, 8))
		self.assertEqual(Frac(0, 3) * Frac(4, 2), Frac(0, 1))	
	
	def test_dzielenie(self):
		self.assertEqual(Frac(1, 2) / Frac(3, 4), Frac(2, 3))
		self.assertEqual(Frac(0, 2) / Frac(3, 4), Frac(0, 1))
		self.assertEqual(Frac(-1, 3) /Frac(6, 7), Frac(-7, 18))

	def test_operatory_jednoargumentowe(self):
		self.assertEqual(-Frac(1, 2), Frac(-1, 2))
		self.assertEqual(~Frac(1, 2), Frac(2, 1))
	
	def test_float(self):
		self.assertEqual(float(Frac(1, 2)), 0.5)
		self.assertEqual(float(Frac(-3, 4)), -0.75)

if __name__ == '__main__':
	unittest.main()
