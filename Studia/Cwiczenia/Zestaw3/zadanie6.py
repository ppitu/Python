def pobierz_liczbe(string):
	number = input(string)
	
	try:
		number = int(number)
	except ValueError:
		print('Nie podano liczby')
	else:
		return number

wiersz = pobierz_liczbe("Podaj ile wierszy: ")
kolumny = pobierz_liczbe("Podaj ile kolumn: ")

string = ''

for x in range(wiersz):
	string += '+' + '----+' * (kolumny) + '\n' + '|' + '    |' * (kolumny) + '\n'

string += '+' + '----+' * (kolumny) + '\n'

print(string)
