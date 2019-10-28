
def roman2int(liczba):
	slownik = { 'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C':100, 'D':500, 'M':1000}

	wynik = 0

	for i in range(len(liczba)):
		if i + 1 < len(liczba) and slownik[liczba[i]] < slownik[liczba[i]]:
			wynik -= slownik[liczba[i]]
		else:
			wynik += slownik[liczba[i]]
	
	return wynik

def test(liczba):
	"""Funcja konerwtuje z rzymskich na arabskie
	>>> test('I')
	1
	>>> test('V')
	5
	>>> test('X')
	10
	>>> test('L')
	50
	>>> test('C')
	100
	>>> test('D')
	500
	>>> test('M')
	1000
	>>> test('VIII')
	8
	>>> test('MDCLXVI')
	1666
	"""

	print(roman2int(liczba))

if __name__ == '__main__':
	#testy
	import doctest
	doctest.testmod()

