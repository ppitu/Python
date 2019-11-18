

def solve1(a, b, c):
	"""Rozwiazywanie rownania liniowego a x + b y + c = 0"""

	if a == 0:
		return [0, -c/b]

	if b == 0:
		return [-c/a, 0]

	return [[-c/a, 0], [0, -c/b]]


print('Test funkcji solve dla a = 2, b = 1, c = -1')
print(solve1(2, 1, -1))
print('Test funckji solve dla a = 63, b = -7 c = 14')
print(solve1(63, -7, 14))
print('Test funkcji solve dla a = 0, b = 0.5, c = 11')
print(solve1(0, 0.5, -11))
print('Test funckji solbe dla a = 0.5, b = 0, c = 11')
print(solve1(0.5, 0, -11))
