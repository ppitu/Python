
def flatten(sequence):
	lista = []

	for x in range(len(sequence)):
		if isinstance(sequence[x], (list, tuple)):
			lista += flatten(sequence[x])
		else:
			lista += [sequence[x]]

	return lista

def test(sequence):
	"""Funckja splaszcza sekwencje
	>>> test([1, 2, [3, 4], 5])
	[1, 2, 3, 4, 5]
	>>> test((1, 2, [3, (4, 5), 6], 7))
	[1, 2, 3, 4, 5, 6, 7]
	>>> test([])
	[]
	>>> test([[[[[1], 2], 3], 4], 5])
	[1, 2, 3, 4, 5]
	"""

	print(flatten(sequence))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
