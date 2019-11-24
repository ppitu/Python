from random import *

def losowa_lista_a(N):
	lista = []

	for x in range(N):
		lista.append(x)

	shuffle(lista)

	return lista

def losowa_lista_b(N):
	lista = []

	for x in range(N - 2):
		lista.append(x + 2)

	lista.append(0)
	lista.append(1)

	return lista

def losowa_lista_c(N):
	lista = losowa_lista_b(N)

	lista.reverse()

	return lista

def losowa_lista_d(N):
	lista = []

	for x in range(N):
		lista.append(gauss(N, N))

	return lista

def losowa_lista_e(N):
	zmienna = randint(1, int(N/2))

	zbior = []

	for x in range(zmienna):
		zbior.append(x)

	lista = []

	for x in range(N):
		lista.append(zbior[randint(0, zmienna - 1)])

	return lista

