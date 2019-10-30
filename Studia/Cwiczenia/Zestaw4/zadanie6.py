
def sum_seq(sequence):
	suma = 0
	
	for x in range(len(sequence)):
		if isinstance(sequence[x], (list, tuple)):
			suma += sum_seq(sequence[x])
		else:
			suma += sequence[x]

	return suma
		

def test(sek):
	""" Funkcja oblicze sume liczb w danej sekwencji 
	>>> test([1])
	1
	>>> test([0])
	0
	>>> test([1, 2, 3, [4, 5]])
	15
 	>>> test([1, (1, 2), [1, (1, 2, [1, 4])]])
	13
	"""

	print(sum_seq(sek))

if __name__ == '__main__':
	import doctest
	doctest.testmod()
