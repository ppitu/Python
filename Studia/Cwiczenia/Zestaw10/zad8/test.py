from randomqueue import *
from random import *
import os

def number(string):
	while True:
		var = input(string)
		
		try: 
			liczba = int(var)
		except ValueError:
			print('Nie podano liczby, sprobuj jeszcze raz')
		else:
			return liczba

queue = RandomQueue()

print('Test kolejki randomowej')

x = number('Podaj ile razy chcesz wywolac program: ')

for var in range(x):
	os.system("clear")
	z = number('Ile elementow dodac do kolejki: ')

	print('Dodawanie elementow')

	for i in range(z):
		print('Dodawanie: ' + str(i))
		queue.insert(i)

	z = number('Ile elementow chcesz usunac: ')

	for i in range(z):
		try:
			print(queue.remove())
		except IndexError:
			print('Proba usuniecia nieistniejacego elementu')
			input('Nacisnij eneter zeby kontynuowac')
			input()
			break 


queue.insert(1)

print('\n\n\n\nSprawdzenie czy kolejka jest pusta')
print(queue.is_empty())
print('Wywolanie metody clear()')
queue.clear()
print('Sprawdzenie czy pusta')
print(queue.is_empty())
