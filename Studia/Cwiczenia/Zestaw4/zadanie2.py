#Zadanie 3.5

def rysuj(n):
	string = '|' + '....|' * n + '\n'
	string += str(0)

	for x in range(n):
		string += str(x + 1).rjust(5)

	return string

print("Zadanie 3.5:")
dlugosc = input('Podaj dlugosc: ')
dlugosc = int(dlugosc)
print(rysuj(dlugosc))


#Zadanie 3.6

def pobierz_liczbe(string):
	number = input(string)
	
	try:
		number = int(number)
	except ValueError:
		print('Nie podano liczby')
	else:
		return number

def rysuj1():
	string = ''
	
	wiersz = pobierz_liczbe('Podaj ile wierszy: ')
	kolumny = pobierz_liczbe('Podaj ile kolumn: ')

	for x in range(wiersz):
		string += '+' + '----+' * (kolumny) + '\n' + '|' + '    |' * (kolumny) + '\n'

	string += '+' + '----+' * (kolumny) + '\n'

	return string

print("Zadanie 3.6:")
print(rysuj1())
