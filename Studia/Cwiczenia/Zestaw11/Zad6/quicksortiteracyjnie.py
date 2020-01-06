

def partition(tab, low, high):
	i = (low - 1)
	x = tab[high]

	for j in range(low, high):
		if tab[j] <= x:
			i = i + 1
			tab[i], tab[j] = tab[j], tab[i]

	tab[i+1], tab[high] = tab[high], tab[i+1]
	return (i + 1)

#tab[] --> tablica do posortowania
#low --> Index poczatkowy
#high --> Index koncowy

def quickSort(tab, low, high):
	#Tworzenie pomocniczego stosu
	size = high - low + 1
	stos = [0] * (size)

	top = -1

	top = top + 1
	stos[top] = low
	top = top + 1
	stos[top] = high

	while top >= 0:
		high = stos[top]
		top = top -1
		low = stos[top]
		top = top -1

		p = partition(tab, low, high)

		if p - 1 > low:
			top = top + 1
			stos[top] = low
			top = top + 1
			stos[top] = p - 1

		if p + 1 < high:
			top = top - 1
			stos[top] = p + 1
			top = top + 1
			stos[top] = high


tab = [5, 2, 34,  6, 88, 8, 8, 3]
print("Tablica przed sortowaniem")
print(tab)

n = len(tab)

quickSort(tab, 0, n - 1)

print("Tablica posortowana")
print(tab)
