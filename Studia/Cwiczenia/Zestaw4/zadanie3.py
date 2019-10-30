
def factorial(n):
	if n == 0:
		return 0
	zmienna = 1
	for x in range(1, n+1):
		zmienna *= x

	return zmienna

print("Dla n = 0: ")
print(factorial(0))

print("Dla n = 1: ")
print(factorial(1))

print("Dla n = 6: ")
print(factorial(6))
