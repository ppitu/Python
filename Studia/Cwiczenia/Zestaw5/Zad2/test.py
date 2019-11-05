import fracs


def test(frac1, frac2):
	"""Funkcja testuje dodwanie ulamkow
	>>> test([1, 2], [2, 3])
	[7.0, 6.0]
	>>> test([0, 2], [2, 3])
	[2.0, 3.0]
	>>> test([1, 2], [1, 2])
	[1.0, 1.0]
	"""

	print(fracs.add_frac(frac1, frac2))

def test1(frac1, frac2):
	"""Funckja testuje odejmowanie ulamkow
	>>> test1([1, 2], [2, 3])
	[-1.0, 6.0]
	>>> test1([1, 2], [-1, 2])
	[1.0, 1.0]
	>>> test1([-1, 2], [2, 3])
	[-7.0, 6.0]
	"""

	print(fracs.sub_frac(frac1, frac2))

def test2(frac1, frac2):
	"""Funckja testuje mnozenie ulamkow
	>>> test2([1, 2], [-2, 3])
	[-1.0, 3.0]
	>>> test2([0, 2], [-1, 2])
	[0.0, 1.0]
	>>> test2([-1, 2], [2, 3])
	[-1.0, 3.0]
	"""

	print(fracs.mul_frac(frac1, frac2))

def test3(frac1, frac2):
	"""Funckja testuje dzielenie ulamkow
	>>> test3([1, 2], [2, 3])
	[3.0, 4.0]
	>>> test3([0, 2], [-1, 2])
	[0.0, 1.0]
	>>> test3([1, 2], [1, 2])
	[1.0, 1.0]
	"""

	print(fracs.div_frac(frac1, frac2))

def test4(frac):
	"""Funckja testuje czy ulamek jest dodatni
	>>> test4([1, 2])
	True
	>>> test4([-1, 2])
	False
	"""

	print(fracs.is_positive(frac))


def test5(frac1, frac2):
	"""Funkcja porownuje ulamki
	>>> test5([1, 4], [2, 4])
	-1
	>>> test5([1, 2], [1, 2])
	0
	>>> test5([2, 4], [1, 4])
	1
	"""

	print(fracs.cmp_frac(frac1, frac2))

def test6(frac):
	"""Funkcja zmienia ulamki z liczby dziesietne
	>>> test6([1, 2])
	0.5
	>>> test6([2, 2])
	1.0
	"""
	
	print(fracs.frac2float(frac))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
