from fracs import *

import unittest

class TestFrac(unittest.TestCase):
	
	def test_yrowna0(self):
		self.assertEqual(str(Frac(1, 2)), '1/2')
		#self.assertEqual(str(Frac(1, 0)), '1')

	def tes_str_repr(self):
		self.assertEqual(str(Frac(1, 3)), '1/3')
		self.assertEqual(repr(Frac(1, 3)), 'Frac(1, 3)')

	def test_operatory_porownanie(self):
		self.assertFalse(Frac(1, 2) == Frac(3, 4))
		self.assertTrue(Frac(1, 2) != Frac(3, 4))
		self.assertTrue(Frac(1, 2) < Frac(3, 4))
		self.assertTrue(Frac(1, 2) <= Frac(3, 4))
		self.assertFalse(Frac(1, 3) > Frac(3, 4))
		self.assertFalse(Frac(1, 2) >= Frac(3, 4))

	def test_dodawanie(self):
		self.assertEqual(Frac(1, 2) + Frac(3, 4), Frac(5, 4))
		self.assertEqual(Frac(0, 3) + Frac(4, 2), Frac(2, 1))
		self.assertEqual(Frac(1, 2) + 1, Frac(3, 2))
		self.assertEqual(1 + Frac(1, 2), Frac(3, 2))
		self.assertEqual(Frac(1, 2) + 0.5, 1)
	
	def test_odejmownie(self):
		self.assertEqual(Frac(1, 2) - Frac(3, 4), Frac(-1, 4))
		self.assertEqual(Frac(0, 3) - Frac(4, 2), Frac(-2, 1))
		self.assertEqual(Frac(1, 2) - 1, Frac(-1, 2))
		self.assertEqual(1 - Frac(1, 2), Frac(1, 2))
		self.assertEqual(Frac(1, 2) - 0.5, 0)

	def test_mnozenie(self):
		self.assertEqual(Frac(1, 2) * Frac(2, 1), Frac(1, 1))
		self.assertEqual(Frac(3, 4) * Frac(0, 3), Frac(0, 1))
		self.assertEqual(Frac(1, 2) * 2, Frac(1, 1))
		self.assertEqual(Frac(1, 2) * 0.5, 0.25)
	
	def test_dzielenie(self):
		self.assertEqual(Frac(1, 2)/Frac(2, 3), Frac(3, 4))
		self.assertEqual(Frac(0, 3)/Frac(3, 4), Frac(0, 1))
		self.assertEqual(Frac(1, 2)/0.5, 1)
		self.assertEqual(0.5/Frac(1, 2), 1)

	def test_negacja(self):
		self.assertEqual(-Frac(1, 2), Frac(-1, 2))	
	
	def test_odwrotnosc(self):
		self.assertEqual(~Frac(1, 2), Frac(2, 1))
		
	def test_float(self):
		self.assertEqual(float(Frac(1, 2)), 0.5)
		self.assertEqual(float(Frac(-3, 4)), -0.75)

if __name__ == '__main__':
	unittest.main()
