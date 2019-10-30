
def odwracanie(lista, left, right):
	lista = lista[:left] + lista[left:right][::-1] + lista[right:]
	return lista

def odwracanieRekurencyjnie(lista, left, right):
	if left >= right or left >= len(lista) or right <= 0:
		return lista

	#lista[left] = lista[right]
	#lista[right] = lista[left]

	lista[left], lista[right] = lista[right], lista[left]

	return odwracanieRekurencyjnie(lista, left + 1, right - 1)	

def test1(lista, left, right):
	"""Funkcja odwraca czesc elementow w liscie iteracyjnie
	>>> test1([1, 2, 3, 4, 5, 6, 7, 8], 1, 4)	
	[1, 4, 3, 2, 5, 6, 7, 8]
	>>> test1([1, 2], 0, 0)
	[1, 2]
	>>> test1([1, 2], 0, 2)
	[2, 1]
	"""

	print(odwracanie(lista, left, right))


def test2(lista, left, right):
	"""Funkcja odwraca czesc elementow na liscie rekurencyjnie
	>>> test2([1, 2, 3, 4, 5, 6, 7, 8], 1, 4)
	[1, 5, 4, 3, 2, 6, 7, 8]
	>>> test2([1, 2, 3, 4], 0, 3)
	[4, 3, 2, 1]
	"""

	print(odwracanieRekurencyjnie(lista, left, right))

if __name__ == '__main__':
	#testy
	import doctest
	doctest.testmod()

L = [1, 2, 3, 4, 5, 6, 7, 8]

print(odwracanie(L, 1, 4))
