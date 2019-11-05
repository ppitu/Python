from fracs import*


def test(x, y):
	"""Funckja testuje wypisanie punktu
	>>> test(1, 2)
	1/2
	Frac(1, 2)
	>>> test(3, 1)
	3
	Frac(3, 1)
	"""

	ft = Frac(x, y)
	print(str(ft))
	print(repr(ft))


def test1(x, y, x1, y1):
	"""Funckja testuje dodawanie obiektow
	>>> test1(1, 2, 2, 3)
	7.0/6.0
	>>> test1(0, 3, 3, 4)
	3.0/4.0
	>>> test1(2, 8, 4, 8)
	3.0/4.0
	"""
	ft1 = Frac(x, y)
	ft2 = Frac(x1, y1)

	print(ft1+ft2)

def test2(x, y, x1, y1):
	"""funkcja testuje odejmowanie elementow
	>>> test2(1, 2, 3, 4)
	-1.0/4.0
	>>> test2(0, 3, 2, 9)
	-2.0/9.0
	>>> test2(4, 5, 0, 2)
	4.0/5.0
	"""
	ft1 = Frac(x, y)
	ft2 = Frac(x1, y1)

	print(ft1-ft2)


def test3(x, y, x1, y1):
	"""Funckja testuje mnozenie elementow
	>>> test3(1, 2, 3, 4)
	3.0/8.0
	>>> test3(0, 3, 4, 2)
	0.0
	>>> test3(-3, 2, 3, 4)
	-9.0/8.0
	"""

	ft1 = Frac(x, y)
	ft2 = Frac(x1, y1)

	print(ft1*ft2)
	

def test4(x, y, x1, y1):
	"""Funkcja testuje dzielenie obiektow
	>>> test4(1, 2, 3, 4)
	2.0/3.0
	>>> test4(0, 2, 3, 4)
	0.0
	>>> test4(-1, 3, 6, 7)
	-7.0/18.0
	"""

	ft1 = Frac(x, y)
	ft2 = Frac(x1, y1)

	print(ft1/ft2)

def test5(x, y):
	"""funckja testuje operatory jednoargumentowe w kolejnosci +, -, ~
	>>> test5(1, 2)
	1/2
	-1.0/2.0
	2.0
	>>> test5(-4, 5)
	-4/5
	4.0/5.0
	5.0/-4.0
	"""

	ft1 = Frac(x, y)

	print(ft1)
	print(-ft1)
	print(~ft1)

def test6(x, y):
	"""Funckja testuje zamiane ulamaka na liczbe zmiennoprzecinkowa
	>>> test6(1, 2)
	0.5
	>>> test6(-3, 4)
	-0.75
	"""

	ft = Frac(x, y)

	print(float(ft))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
