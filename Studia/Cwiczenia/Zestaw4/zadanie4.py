
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


print("Ciag dla n = 0")
print(fibonacci(0))

print("Ciag dla n = 2")
print(fibonacci(2))

print("Ciag dla n = 10")
print(fibonacci(10))
