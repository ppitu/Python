name = ""
while name != 'stop':
	name = input('Podaj liczbe lub napisz stop: ')
	if name == 'stop':
		break
	try:
		name = float(name)
	except ValueError:
		print('Nie podano lczby')
	else:
		print(name, name**3)
