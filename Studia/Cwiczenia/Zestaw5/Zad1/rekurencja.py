def factorial(n):
	if n == 0:
		return 0
	zmienna = 1
	for x in range(1, n+1):
		zmienna *= x

	return zmienna


def fibonacci(n):
	if n == 0 or n == 1:
		return n
	
	f1 = 1
	f2 = 1
	tmp = 0

	for x in range(3,n+1):
		tmp = f1+f2
		f1 = f2
		f2 = tmp
	return f2
