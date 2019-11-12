from singlelist import*

alist = SingleList()

print("Dodanie elementow na poczatku listy")
alist.insert_head(Node(11))
alist.insert_head(Node(22))
alist.insert_head(Node(22))
alist.insert_head(Node(44))
print("dodanie elementow na koniec listy")
alist.insert_tail(Node(55))
alist.insert_tail(Node(66))
alist.insert_tail(Node(77))
print("length po dodaniu elementow", alist.length)
print("Ostatnie", alist.remove_tail()) # wykorzystujemy interfejs
print('Usuniecie wszytskich elementow listy')
while not alist.is_empty():   # kolejność 22, 11, 33
    print("remove head", alist.remove_head())

try:
	print('Proba usuniecia elementu z postej listy (remove_tail())')
	alist.remove_tail()
	print('Usunieto')
except ValueError:
	print('Usuwanie z pustej listy')

print("uzupelnianie listy")
alist.insert_tail(Node(11))
alist.insert_tail(Node(22))
alist.insert_tail(Node(33))

blist = SingleList()

print('Uzuniepnianie drugiej listy')

blist.insert_tail(Node(44))
blist.insert_tail(Node(55))
blist.insert_tail(Node(66))

print('Wielkosc alist ', alist.count())

print('Laczenie list')

alist.merge(blist)

print('Wielkosc alist ', alist.count())

print('Usunie elementow z alisty')
while not alist.is_empty():
	print("remove tail", alist.remove_head())

print('Wielkosc blist przed usunieciem: ', blist.count())

print('Usuniecie listy alist za pomoca clear()')
blist.clear()
print('Wielkosc blist: ', blist.length)
