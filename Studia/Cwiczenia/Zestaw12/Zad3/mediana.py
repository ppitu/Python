
def mediana_sort(L, left, right):
	Li = L[left:right]

	Li.sort()

	if len(Li) % 2 == 0:
		return Li[int((len(Li)/2))]
	else:
		return Li[int((len(Li)+1)/2)]


lista = []

for x in range(100):
	lista.append(x + 1)

print('Szukanie mediany dla listy 100 elementow')
print(mediana_sort(lista, 49, 99))
