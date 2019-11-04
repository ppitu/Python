from rectangles import *

def test(x1, y1, x2, y2):
	"""Funckja testuje wypiwywanie prostokata
	>>> test(1, 2, 3, 4)
	[(1, 2), (3, 4)]
	Rectangle(1, 2, 3, 4)
	"""
	
	pt1 = Rectangle(x1, y1, x2, y2)

	print(str(pt1))
	print(repr(pt1))


def test1(x1, y1, x2, y2, x11, y11, x22, y22):
	"""Funckja testuj porównywanie prostokatow
	>>> test1(1, 2, 3, 4, 5, 6, 7, 8)
	False
	True
	>>> test1(1, 1, 2, 2, 1, 1, 2, 2)
	True
	False
	"""

	pt1 = Rectangle(x1, y1, x2, y2)
	pt2 = Rectangle(x11, y11, x22, y22)

	print(pt1 == pt2)
	print(pt1 != pt2)

def test2(x1, y1, x2, y2):
	"""Funkcja testuje obliczanie srodku prostokata
	>>> test2(1, 2, 4, 5)
	(2.5, 3.5)
	>>> test2(4, 4, 5, 5)
	(4.5, 4.5)
	"""

	pt1 = Rectangle(x1, y1, x2, y2)

	print(pt1.center())

def test3(x1, y1, x2, y2):
	"""Funkcja testuje liczenia pola powierzchni
	>>> test3(0, 2, 3, 4)
	6
	>>> test3(2, 2, 4, 4)
	4
	"""

	pt1 = Rectangle(x1, y1, x2, y2)

	print(pt1.area())

def test4(x1, y1, x2, y2, x, y):
	"""Funckja testuje przesuniecie figury
	>>> test4(1, 2, 3, 4, 1, 2)
	[(2, 4), (4, 6)]
	>>> test4(1, 2, 3, 4, 0, 0)
	[(1, 2), (3, 4)]
	>>> test4(1, 3, 4, 6, -1, -3)
	[(0, 0), (3, 3)]
	"""

	pt1 = Rectangle(x1, y1, x2, y2)

	print(pt1.move(x, y))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
