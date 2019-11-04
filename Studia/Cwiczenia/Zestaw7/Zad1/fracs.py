
class Frac:
	"""Klasa reprezentujaca ulamki"""

	def __init__(self, x = 0, y = 1):
		try:
			if y == 0:
				raise ZeroDivisionError
			self.x = x
			self.y = y
		except	ZeroDivisionError:
			print("Nie mozna przypisac zera do mianownika")
			print("Ulamek zostaje ustawiony na 1")
			self.x = 1
			self.y = 1

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
	
	def __gt__(self, other):		#operator >
		return self.x/self.y > other.x/other.y

	def __ge__(self, other):		#operator >=
		return self.x/self.y >= other.x/other.y

	def __add__(self, other):
		if isinstance(other, int) or isinstance(other, float) or isinstance(other, long):
			return Frac(self.x + other*self.y, self.y)
		if self.x == 0:
			return other
		if other.x == 0:
			return self
		if self.y == other.y:
			return Frac(self.x + other.x, self.y)
		
		return Frac(self.x*other.y + other.x*self.y, self.y*other.y)
