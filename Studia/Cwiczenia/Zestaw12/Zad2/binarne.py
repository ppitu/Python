def binarne_rek(L, left, right, y):
	"""Wyszukiwanie binarne w wersji rekurencyjne"""

	k = int((left+right)/2)

	if left == right:
		return None

	if y == L[k]:
		return k
	elif y > L[k]:
		return binarne_rek(L, k + 1, right, y)
	else:
		return binarne_rek(L, left, k - 1, y)


lista = []

for x in range(100):
	lista.append(x)
print('Wyszukanie 56 w tablicy elementow od 0 do 99')
print(binarne_rek(lista, 0, 99, 56))
print('wyszukanie 1000 w tablicy elementow od 0 do 99')
print(binarne_rek(lista, 0, 99, 1000))
