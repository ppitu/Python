from points import Point

class Rectangle:
	"""Klasa reprezentuje prostokat na plaszczyznie"""

	def __init__(self, x1, y1, x2, y2):
		if x1 > x2 or y1 > y2:
			raise ValueError

		self.pt1 = Point(x1, y1)
		self.pt2 = Point(x2, y2)

	def __str__(self):	#"[(x1, y1), (x2, y2)]"
		return "[({}, {}), ({}, {})]".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

	def __repr__(self):	#Rectangle(x1, y1, x2, y2)
		return "Rectangle({}, {}, {}, {})".format(self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

	def __eq__(self, other):
		return self.pt1 == other.pt1 and self.pt2 == other.pt2	
	
	def __ne__(self, other):
		return not self == other

	def center(self):	#zwraca srodek
		return Point((self.pt2.x + self.pt1.x)/2, (self.pt2.y + self.pt1.y)/2)

	def area(self):		#pole powierzchni
		return (self.pt2.y - self.pt1.y)*(self.pt2.x - self.pt1.x)

	def move(self, x, y):
		return Rectangle(self.pt1.x + x, self.pt1.y + y, self.pt2.x + x, self.pt2.y + y)	
	def intersection(self, other):		#czesc wspolna prostokatow
		if self.pt1.x < other.pt1.x:
			return Rectangle(other.pt1.x, other.pt1.y, self.pt2.x, self.pt2.y)
		else:
			return Rectangle(self.pt1.x, self.pt1.y, other.pt2.x, other.pt2.y)

	def cover(self, other):
		return Rectangle(self.pt1.x, self.pt1.y, other.pt2.x, other.pt2.y)

	def make4(self): 
		lista = []
		srd = Point((self.pt2.x + self.pt1.x)/2, (self.pt1.y + self.pt2.y)/2)
		
		lista.append(Rectangle(self.pt1.x, self.pt1.y, srd.x, srd.y))
		lista.append(Rectangle(srd.x, srd.y, self.pt2.x, self.pt2.y))
		lista.append(Rectangle(self.pt1.x, srd.y, srd.x, self.pt2.y))
		lista.append(Rectangle(srd.x, self.pt1.y, self.pt2.x, srd.y))
	
		return lista	
