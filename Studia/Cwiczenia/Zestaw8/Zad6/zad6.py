
class PClass:
	def __init__(self):
		self.cache = {0 : {0 : 0.5 }}

	def __call__(self, i, j):
		if i == 0 and j == 0:
			return self.cache[0][0]

		if i == 0 and j != 0:
			self.cache[0] = {j : 1.0}
			return self.cache[0][j]

		if i != 0 and j == 0:
			self.cache[i] = {0 : 0.0}
			return self.cache[i][0]
		
		if i not in self.cache:
			self.cache[i][j] = (0.5*(self(i - 1, j) + self(i, j - 1)))			
		return self.cache[i][j]


pcl = PClass()

print('Test dla P(0, 0)')
print(pcl(0, 0))
print('Test dla P(0, 4)')
print(pcl(0, 4))
print('Test dla P(4, 0)')
print(pcl(4, 0))
print('Test dla P(2, 3)')
print(pcl(2, 3))
print('Test dla P(3, 2)')
print(pcl(3, 2))
