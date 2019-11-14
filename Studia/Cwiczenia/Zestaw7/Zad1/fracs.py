from math import gcd

'''def nwd(x, y):
	zmienna = gcd(x, y)
	return Frac(x/zmienna, y/zmienna)'''


class Frac:
	"""Klasa reprezentujaca ulamki"""

	def __init__(self, x = 0, y = 1):
		try:
			if y == 0:
				raise ZeroDivisionError
			zmienna = gcd(x, y)
			if zmienna != 1:
				self.x = int(x/zmienna)
				self.y = int(y/zmienna)
			else:
				self.x = x
				self.y = y
		except	ZeroDivisionError:
			print("Error Dzielenie Przez Zero")

	def __str__(self):
		if self.y == 1:
			return "{}".format(self.x)
		if self.x == 0:
			return "{}".format(self.x)
		return "{}/{}".format(self.x, self.y)

	def __repr__(self):
		return "Frac({}, {})".format(self.x, self.y)

	def __eq__(self, other):		#operator ==
		return self.x == other.x and self.y == other.y

	def __ne__(self, other):		#operator !=
		return not self == other
	
	def __lt__(self, other):		#operator <
		return self.x/self.y < other.x/other.y
	
	def __le__(self, other):		#operaotr <=
		return self.x/self.y <= other.x/other.y
	
	def __add__(self, other):
		if isinstance(other, int):
			return Frac(self.x + other*self.y, self.y)
		if isinstance(other, float):
			return self.x/self.y + other
		if self.x == 0:
			return Frac(other.x, other.y)
		if other.x == 0:
			return Frac(self.x, self.y)
		if self.y == other.y:
			return Frac(self.x + other.x, self.y)
		
		return Frac(self.x*other.y + other.x*self.y, self.y*other.y)

	__radd__ = __add__

	def __sub__(self, other):
		if isinstance(other, int):
			return Frac(self.x - other*self.y, self.y)
		if isinstance(other, float):
			return self.x/self.y - other
		if self.x == 0:
			return Frac(-other.x, other.y)
		if other.x == 0:
			return Frac(self.x, self.y)
		if self.y == other.y:
			return Frac(self.x - other.x, self.y)

		return Frac(self.x*other.y - other.x*self.y, self.y*other.y)		
	
	def __rsub__(self, other):
		
		return Frac(self.y*other - self.x, self.y)

	def __mul__(self, other):
		if isinstance(other, int):
			return Frac(self.x*other, self.y)
		if isinstance(other, float):
			return self.x/self.y * other
		if self.x == 0 or other.x == 0:
			return Frac(0, self.y)
		return Frac(self.x*other.x, self.y*other.y)

	__rmul__ = __mul__

	def __truediv__(self, other):
		if isinstance(other, int):
			try:
				if other == 0:
					raise ZeroDivisionError
				return Frac(self.x, self.y*other)
			except ZeroDivisionError:
				print("Dzielenie przez zero")
				return Frac(1, 1)
		if isinstance(other, float):
			try:
				if other == 0.0:
					raise ZeroDivisionError
				return (self.x/self.y)/other
			except ZeroDivisionError:
				print("Dzielenie przez zero")
				return Frac(1, 1)
		if self.x == 0:
			return Frac(0, 1)

		return Frac(self.x*other.y, self.y*other.x)

	def __rtruediv__(self, other):
		if isinstance(other, int):
			try:
				if other == 0:
					raise ZeroDivisionError
				return Frac(self.x, self.y*other)
			except ZeroDivisionError:
				print("Dzielenie przez zero")
				return Frac(1, 1)
		if isinstance(other, float):
			try:
				if other == 0.0:
					raise ZeroDivisionError
				return (self.x/self.y)/other
			except ZeroDivisionError:
				print("Dzielenie przez zero")
				return Frac(1, 1)
	
		if self.x == 0:
			return Frac(0, 1)
		
		return Frac(self.x*other.y, self.y*other.x)
	
	#operatory jednoargumentowe
	
	def __pos__(self):
		return self

	def __neg__(self):
		return Frac(-self.x, self.y)

	def __invert__(self):
		return Frac(self.y, self.x)

	def __float__(self):
		return self.x/self.y
