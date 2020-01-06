import random

def bogoSort(tab):
	n = len(tab)
	while (is_sorted(tab) == False):
		shuffle(tab)

def is_sorted(tab):
	n = len(tab)
	for i in range(0, n - 1):
		if(tab[i] > tab[i + 1]):
			return False
	return True

def shuffle(tab):
	n = len(tab)
	for i in range(0, n):
		r = random.randint(0, n - 1)
		tab[i], tab[r] = tab[r], tab[i]


tab = [3, 4, 5, 1, 3, 8]
print("Tablica przed sortowaniem")
print(tab)
bogoSort(tab)
print("Posortowana tablica")
print(tab)
