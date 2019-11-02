from points import *


def test(x, y):
	"""funckja testuje __str__ oraz __repr__
	>>> test(1, 0)
	(1, 0)
	Point(1, 0)
	"""

	p1 = Point(x, y)
	print(str(p1))
	print(repr(p1))

def test1(x, y, z, v):
	"""Funckja testue porownywanie punktow
	>>> test1(2, 0, 3, 4)
	False
	True
	>>> test1(1, 3, 1, 3)
	True
	False
	"""

	p1 = Point(x, y)
	p2 = Point(z, v)

	print(p1 == p2)
	print(p1 != p2)

def test2(x, y, z, v):
	"""Funckja testuje dodawanie wektorow
	>>> test2(2, 0, 3, 4)
	(5, 4)
	>>> test2(-3, 2, 5, 19)
	(2, 21)
	"""

	v1 = Point(x, y)
	v2 = Point(z, v)

	print(v1 + v2)

def test3(x, y, z, v):
	"""Funckja testuje odejmowanie wektorow
	>>> test3(2, 0, 3, 4)
	(-1, -4)
	>>> test3(4, 5, 1, 1)
	(3, 4)
	"""
	
	v1 = Point(x, y)
	v2 = Point(z, v)

	print(v1 - v2)

def test4(x, y, z, v):
	"""Funckja testuje iloczyn skalarny wektorow
	>>> test4(2, 0, 3, 4)
	6
	>>> test4(2, 6, 3, 1)
	12
	"""

	v1 = Point(x, y)
	v2 = Point(z, v)

	print(v1*v2)

def test5(x, y, z, v):
	"""Funckja testuje iloczyn wektorowy 
	>>> test5(2, 0, 3, 4)
	8
	>>> test5(4, 5, 2, 6)
	14
	"""

	v1 = Point(x, y)
	v2 = Point(z, v)

	print(v1.cross(v2))

def test6(x, y):
	"""Funckja testuje dlugosc wektor
	>>> test6(0, 2)
	2.0
	>>> test6(3, 4)
	5.0
	"""

	v1 = Point(x, y)

	print(v1.length())

if __name__ == '__main__':
	import doctest
	doctest.testmod()
