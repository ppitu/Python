import math

def nwd(x, y):
	zmienna = math.gcd(x, y)

	return Frac(x/zmienna, y/zmienna)

class Frac:
	"""Klasa reprezentujaca ulamek."""
	def __init__(self, x = 0, y = 0):
		self.x = x
		self.y = y

	
	def __str__(self):
		if self.y == 1:
			return "{}".format(self.x)
		else:
			return "{}/{}".format(self.x, self.y)

	def __repr__(self):
		return "Frac({}, {})".format(self.x, self.y)

	def __add__(self, other):
		if other.x == 0:
			return nwd(self.x, self.y)
		if self.x == 0:
			return nwd(other.x, other.y)

		if self.y == other.y:
			return nwd(self.x + other.x, self.y)
		else:
			return nwd(self.x*other.y + other.x*self.y, self.y*other.y)

	def __sub__(self, other):
		if self.x == 0:
			return nwd(-other.x, other.y)
		if other.x == 0:
			return nwd(self.x, self.y)
		if self.y == other.y:
			return nwd(self.x - other.x, self.y)
		else:
			return nwd(self.x*other.y - other.x*self.y, self.y*other.y)

	def __mul__(self, other):
		return nwd(self.x*other.x, self.y*other.y)

	def __truediv__(self, other):
		return nwd(self.x*other.y, self.y*other.x)

	def __pos__(self):
		return self

	def __neg__(self):
		return nwd(-self.x, self.y)

	def __invert__(self):
		return nwd(self.y, self.x)

	def __eq__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False 
	def __float__(self):
		return self.x/self.y	

	
