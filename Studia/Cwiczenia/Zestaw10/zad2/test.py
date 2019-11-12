from stack import *

stack = Stack()

print('Sprawdzenie czy pusty:', stack.is_empty())

print('Dodanie 10 elementow')
stack.push(0)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(5)
stack.push(6)
stack.push(7)
stack.push(8)
stack.push(9)

print('Sparwdzenie przepelnienia stosu:')
try:
	stack.push(10)
	print('Dodano element')
except IndexError:
	print('Przepelnienie stosu, nie dodano elementu')

print('Sprawdzenie czy pelny: ', stack.is_full())

print('Usuwanie elementow')
while not stack.is_empty():
	print('Element: ', stack.pop())

print('Sprawdzenie usuniecia elementu z pustego stosu')
try:
	stack.pop()
	print('Usunieto element')
except IndexError:
	print('Brak elementow do usuniecia')
