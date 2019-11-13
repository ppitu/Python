from random import *

def monteCarlo(ilosc_losowan):
	
	punktow_w_kole = 0

	for x in range(ilosc_losowan):
		x = uniform(-1.0, 1.0)
		y = uniform(-1.0, 1.0)

		if x*x + y*y <= 1:
			punktow_w_kole += 1

	return 4* punktow_w_kole/ilosc_losowan

print('Dla 10 losowan: ', monteCarlo(10))
print('Dla 100 losowan: ', monteCarlo(100))
print('Dla 1000 losowan: ', monteCarlo(1000))
print('Dla 10000 losowan: ', monteCarlo(10000))
print('Dla 100000 losowan: ', monteCarlo(100000))
print('Dla 1000000 losowan: ', monteCarlo(1000000))
