dlugosc = input('Podaj dlugosc: ')

dlugosc = int(dlugosc)

string = '|' + '....|' * dlugosc + '\n'

string += str(0)

for x in range(dlugosc):
	string += str(x + 1).rjust(5)

print(string)
