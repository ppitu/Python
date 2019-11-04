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
	"""Funckja zwraca srodek prostokata
	>>> test2(1, 2, 2, 5)
	"""

	pt1 = Rectangle(x1, y2, x2, y2)

	print(pt1.center())

if __name__ == '__main__':
	import doctest
	doctest.testmod()
