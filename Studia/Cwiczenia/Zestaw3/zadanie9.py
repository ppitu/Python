def suma(lista):
	"""
	Funckja wypisuje sume wartosci w listach lub krotkach:
	>>> suma([[1, 2]])
	[3]
	>>> suma([[], [4], (1,2), [3,4], (5,6,7)])
	[0, 4, 3, 7, 18]
	"""
	
	newlist = []

	for z in range(len(lista)):
		newlist.append(sum(lista[z]))

	print(newlist)


if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
