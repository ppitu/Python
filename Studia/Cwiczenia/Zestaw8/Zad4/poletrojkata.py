import math

def heron(a, b, c):
	"""Obliczanie pola powierzchni trojkata za pomoca wzory Herona. Dlogosci bokow trojkata wynosza a, b, c."""

	z = max([a, b, c])

	if a == z and b + c < z or b == z and a + c < z or c == z and a + b < c:
		raise ValueError

	p = (a + b + c)/2

	return math.sqrt(p*(p - a)*(p - b)*(p - c))

print('Pole trojkata dla a = 3, b = 4, c = 5: ', heron(3, 4, 5))		
print('Pole trojkata dla a = 5, b = 4, c = 4: ', heron(5, 4, 4))
try:
	print('Obliczanie pola dla a = 5, b = 1, c = 1: ', heron(5, 1, 1))
except ValueError:
	print('Z podanych odcinkow nie mozna stworzyc trojkata')
