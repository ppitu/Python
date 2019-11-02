
def add_frac(frac1, frac2):
	lista = []
	if frac1[0] == 0:
		return frac2
	
	if frac2[0] == 0:
		return frac1

	if frac1[1] == frac2[1]:
		lista += [frac1[0] + frac2[0], frac1[1]]
	else:
		frac1[0], frac2[0] = frac1[0]*frac2[1], frac2[0]*frac1[1]
		frac1[1], frac2[1] = frac1[1]*frac2[1], frac2[1]*frac1[1]
		lista += [frac1[0] + frac2[0], frac1[1]]

	return lista

def sub_frac(frac1, frac2):
	lista = []
	if frac1[0] == 0:
		return frac2
	
	if frac2[0] == 0:
		return frac1

	if frac1[1] == frac2[1]:
		lista += [frac1[0] - frac2[0], frac1[1]]
	else:
		frac1[0], frac2[0] = frac1[0]*frac2[1], frac2[0]*frac1[1]
		frac1[1], frac2[1] = frac1[1]*frac2[1], frac2[1]*frac1[1]
		lista += [frac1[0] - frac2[0], frac1[1]]

	return lista

def mul_frac(frac1, frac2):
	
	if frac1[0] == 0:
		return [0, frac2[1]]
	
	if frac2[0] == 0:
		return [0, frac1[1]]

	return [frac1[0]*frac2[0], frac1[1]*frac2[1]]

def div_frac(frac1, frac2):
	if frac1[0] == 0:
		return [0, frac2[1]]

	return [frac1[0]*frac2[1], frac1[1]*frac2[0]]

def is_positive(frac):
	if frac[0] >= 0:
		return True
	else:
		return False	

def is_zero(frac):
	if frac[0] == 0:
		return True
	else:
		return False

def cmp_frac(frac1, frac2):
	x = frac1[0]/frac1[1]
	y = frac2[0]/frac2[1]

	if x < y:
		return -1
	elif x == y:
		return 0
	else:
		return 1


def frac2float(frac):
	return frac[0]/frac[1]


