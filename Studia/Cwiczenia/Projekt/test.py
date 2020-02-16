from tree import *
import os

myTree = AVLTree()

print("Uzupelnianie drzewa 20 elementami")
for x in range(20):
	print("Dodaje: " + str(x))
	myTree.insert(x) 

input("Nacisnij Enter żeby kontynuować...")
os.system("clear")

print("Rozmiar drzewa: " + str(myTree.sizeTree()))
print("Wyswietlone drzewo:")
myTree.printTree()

input("Nacisnij Enter żeby kontynuować...")
os.system("clear")
print("Usuwanie pierwszy 10 elementow z drzewa")
for x in range(10):
	myTree.delete(x)

print("Wyswietlenie drzewa:")
myTree.printTree()
input("Nacisnij Eneter żeby kontynuować...")
os.system("clear")

print("Tworzenie nowego drzewa i dodanie 20 losowych elementow.")
for x in range(20):
	

"""myTree.insert(10) 
myTree.insert(20) 
myTree.insert(30) 
myTree.insert(40) 
myTree.insert(50) 
myTree.insert(25) 
myTree.insert(18)
myTree.insert(51)
print("\n")
print(myTree.sizeTree())

myTree.printTree();

#myTree.preOrder() 
print("\n")
myTree.delete(50)
myTree.delete(20)
myTree.preOrder()"""
