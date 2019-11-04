from fracs import *

def test(x, y):
	"""Funkcja testuje y = 0
	>>> test(1, 2)
	1/2
	>>> test(1, 0)
	Nie mozna przypisac zera do mianownika
	Ulamek zostaje ustawiony na 1
	1
	"""
	
	ft = Frac(x, y)
	print(str(ft))


def test1(x, y):
	"""Funckja testuje __str__ oraz __repr__
	>>> test1(1, 3)
	1/3
	Frac(1, 3)
	>>> test1(4, 1)
	4
	Frac(4, 1)
	>>> test1(0, 2)
	0
	Frac(0, 2)
	"""

	ft = Frac(x, y)

	print(str(ft))
	print(repr(ft))

def test2(x, y, x1, y1):
	"""Funckja testuje operatory porownania w kolejnosci ==, !=, <, <=, >, >=
	>>> test2(1, 2, 3, 4)
	False
	True
	True
	True
	False
	False
	>>> test2(1, 2, 1, 2)
	True
	False
	False
	True
	False
	True
	>>> test2(3, 4, 1, 2)
	False
	True
	False
	False
	True
	True
	"""

	ft1 = Frac(x, y)
	ft2 = Frac(x1, y1)

	print(ft1 == ft2)
	print(ft1 != ft2)
	print(ft1 < ft2)
	print(ft1 <= ft2)
	print(ft1 > ft2)
	print(ft1 >= ft2)

if __name__ == '__main__':
	import doctest
	doctest.testmod()
