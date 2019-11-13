from queue import *

queue = Queue()

print('Sprawdzenie czy kolejka jest pusta: ', queue.is_empty())
print('Sprawdzanie czy pelna: ', queue.is_full())
print('Dodanie 5 elementow')
queue.put(10)
queue.put(11)
queue.put(12)
queue.put(13)
queue.put(14)

print('Proba dodania elementu poza wielkosc kolejki')
try:
	queue.put(15)
	print('Dodano element')
except IndexError:
	print('Przepelnienie kolejki, nie dodano elementu')

print('Sprawdzenie czy pelna: ', queue.is_full())
print('Sprawdzanie czy pusta: ', queue.is_empty())
print('Usuwanie elementow')

while not queue.is_empty():
	print('Element: ', queue.get())

print('Proba pobrania nie istniejacego elementu')
try:
	queue.get()
	print('Pobrano element')
except IndexError:
	print('Element nie istnieje')
