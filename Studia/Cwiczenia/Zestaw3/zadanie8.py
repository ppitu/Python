def test1(list1, list2):
	"""Funkcja testuje czesc wspolna:
	>>> test1([1,2,3], [4, 5, 6])
	[]
	>>> test1([1,2,3], [2,3,4])
	[2, 3]
	"""
	
	print(czescWspolna(list1, list2))

def test2(list1, list2):
	"""Funckja testuje unie:
	>>> test2([], [1]);
	[1]
	>>> test2([1, 2, 3, 4], [3, 4, 5, 6])
	[1, 2, 3, 4, 5, 6] 
	"""

	print(uniaSekwencji(list1, list2))

def czescWspolna(set1, set2):
	return list(set(set1) & set(set2))

def uniaSekwencji(set1, set2):
	return list(set(set1) | set(set2))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
	
	list1 = [1, 2,3 ,4]
	list2 = [3,4,5]

	list3 = czescWspolna(list1, list2)

	print(list3)

	list3 = uniaSekwencji(list1, list2)

	print(list3)
