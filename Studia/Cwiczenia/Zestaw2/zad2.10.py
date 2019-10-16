import sys

#Zadanie 2.10
def ileWyrazow(line):
	"""Funkcja zwraca liczbe wyrazow rozdzielonych bialymi znakami:
	>>> ileWyrazow('ab')
	1
	>>> ileWyrazow(' ')
	0
	>>> ileWyrazow('ab\tcd\ghas\tlal majest')
	4
	>>> ileWyrazow('ab \
	ab')
	2
	"""

	L = line.split()
	print(len(L))

#Zadanie 2.11
def podziel(word):
	"""Funckja dzieli znaki w wyrazie znakiem '_':
	>>> podziel('test')
	t_e_s_t
	>>> podziel('  ')
	 _ 
	>>> podziel('a')
	a
	"""
	print('_'.join(word))
	
#Zadanie 2.12
def napisZPierwszychLiter(word):
	"""Funkcja ma za zadanie stworzyc wyraz z pierwyszch liter wyrazow w zdaniu:
	>>> napisZPierwszychLiter('test')
	t
	>>> napisZPierwszychLiter('test samochod')
	ts
	>>> napisZPierwszychLiter('ala mam kota')
	amk

	"""
	
	zmienna = ''
	for x in word.split():
		zmienna += list(x)[0]

	print(zmienna)

def napisZOstatnichLiter(word):
	"""Funkcja ma za zdanianie stworzyc wyraz z ostatnich liter wyrazow w zdaniu:
	>>> napisZOstatnichLiter('test')
	t
	>>> napisZOstatnichLiter('test samochod')
	td
	>>> napisZOstatnichLiter('ala ma kota')
	aaa
	"""

	zmienna = ''
	for x in word.split():
		zmienna += list(x)[-1]

	print(zmienna)

#Zadanie 2.13
def dlugoscWyrazow(line):
	"""Funckja zwraca laczna liczbe znakow w zdaniu z pomienieciem bialych znakow:
	>>> dlugoscWyrazow('ala ma kota')
	9
	>>> dlugoscWyrazow('')
	0
	>>> dlugoscWyrazow('alal mama lsllss ksksks')
	20
	"""

	print(sum(map(len, line.split())))

#Zadanie 2.14
def najdluzszyWyraz(line):
	"""Funckja zwraca najdluzszy wyraz:
	>>> najdluzszyWyraz('ala ma kota')
	kota 4
	>>> najdluzszyWyraz('a')
	a 1
	>>> najdluzszyWyraz('ala mam banana')
	banana 6
	"""

	max_word = ''
	max_length = 0

	for x in line.split():
		if len(x) > max_length:
			max_word = x
			max_length = len(x)

	print(max_word + ' ' + str(max_length))

#Zadanie 2.15

#Zadanie 2.16
def zamianaZnakow(line):
	"""Funckja zamienia ciag znakow w tekscie:
	>>> zamianaZnakow('GvR')
	Guido van Rossum
	>>> zamianaZnakow('ala GvR kota')
	ala Guido van Rossum kota
	>>> zamianaZnakow('ala ma kota')
	ala ma kota

	"""

	print(line.replace('GvR', 'Guido van Rossum'))

#Zadanie 2.16

if __name__ == '__main__':
	# testy
	import doctest
	doctest.testmod()
