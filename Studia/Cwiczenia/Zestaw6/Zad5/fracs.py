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
			return Frac(self.x, self.y)
		if self.x == 0:
			return Frac(other.x, other.y)

		if self.y == other.y:
			return Frac(self.x + other.x, self.y) 
		else:
			return Frac(self.x*other.y + other.x*self.y, self.y*other.y)

	def __sub__(self, other):
		if self.x == 0:
			return Frac(-other.x, other.y)
		if other.x == 0:
			return Frac(self.x, other.y)
		if self.y == other.y:
			return Frac(self.x - other.x, self.y)
		else:
			return Frac(self.x*other.y - other.x*self.y, self.y*other.y)

	def __mul__(self, other):
		return Frac(self.x*other.x, self.y*other.y)

	def __div__(self, other):
		return Frac(self.x*other.y, self.y*other.x)

	def __pos__(self):
		return self

	def __neg__(self):
		return Frac(-self.x, self.y)

	def __invert(self):
		return Frac(self.y, self.x)

	def __cmp__(self, other):
		if self.x == other.x and self.y == other.y:
			return True
		else:
			return False 
	def __float__(self):
		return self.x/self.y	

