from losoweliczby import *
from sortowania import *
import time
import os

wyniki = {}

os.system("clear")

print('Select sort dla listy wariant a')
my_list = losowa_lista_a(10**2)
start_time = time.time()
selectsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Select Sort"] = [{"Losowanie a dla 10**2" : czas}]

my_list = losowa_lista_a(10**3)
start_time = time.time()
selectsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie a dla 10**3" : czas})

my_list = losowa_lista_a(10**4)
start_time = time.time()
selectsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie a dla 10**4" : czas})

my_list = losowa_lista_a(10**5)
start_time = time.time()
#selectsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie a dla 10**5" : czas})

my_list = losowa_lista_a(10**6)
start_time = time.time()
#selectsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie a dla 10**6" : czas})

##################################################################################################

os.system("clear")
print('Select Sort dla listy wariant b')

my_list = losowa_lista_b(10**2)
start_time = time.time()
selectsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie b dla 10**2" : czas})

my_list = losowa_lista_b(10**3)
start_time = time.time()
selectsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie b dla 10**3" : czas})

my_list = losowa_lista_b(10**4)
start_time = time.time()
selectsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie b dla 10**4" : czas})

my_list = losowa_lista_b(10**5)
start_time = time.time()
#selectsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie b dla 10**5" : czas})

my_list = losowa_lista_b(10**6)
start_time = time.time()
#selectsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie b dla 10**6" : czas})

#####################################################################################

os.system('clear')
print('Select Sort dla listy warianat c')

my_list = losowa_lista_c(10**2)
start_time = time.time()
selectsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie c dla 10**2" : czas})

my_list = losowa_lista_c(10**3)
start_time = time.time()
selectsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie c dla 10**3" : czas})

my_list = losowa_lista_c(10**4)
start_time = time.time()
selectsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie c dla 10**4" : czas})

my_list = losowa_lista_c(10**5)
start_time = time.time()
#selectsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie c dla 10**5" : czas})

my_list = losowa_lista_c(10**6)
start_time = time.time()
#selectsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie c dla 10**6" : czas})

#####################################################################################

os.system("clear")
print('Select Sort dla listy wariant d')

my_list = losowa_lista_d(10**2)
start_time = time.time()
selectsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie d dla 10**2" : czas})

my_list = losowa_lista_d(10**3)
start_time = time.time()
selectsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie d dla 10**3" : czas})

my_list = losowa_lista_d(10**4)
start_time = time.time()
selectsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie d dla 10**4" : czas})

my_list = losowa_lista_d(10**5)
start_time = time.time()
#selectsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie d dla 10**5" : czas})

my_list = losowa_lista_d(10**6)
start_time = time.time()
#selectsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie d dla 10**6" : czas})

#####################################################################################
os.system("clear")
print('Select sort dla listy wariant e')

my_list = losowa_lista_e(10**2)
start_time = time.time()
selectsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie e dla 10**2" : czas})

my_list = losowa_lista_e(10**3)
start_time = time.time()
selectsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie e dla 10**3" : czas})

my_list = losowa_lista_e(10**4)
start_time = time.time()
selectsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie e dla 10**4" : czas})

my_list = losowa_lista_e(10**5)
start_time = time.time()
#selectsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie e dla 10**5" : czas})

my_list = losowa_lista_e(10**6)
start_time = time.time()
#selectsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Select Sort"].append({"Losowanie e dla 10**6" : czas})

#####################################################################################

os.system("clear")
print('Inster Sort dla listy wariant a')

my_list = losowa_lista_a(10**2)
start_time = time.time()
insertsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"] = [{"Losowanie a dla 10**2" : czas}]

my_list = losowa_lista_a(10**3)
start_time = time.time()
insertsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie a dla 10**3" : czas})

my_list = losowa_lista_a(10**4)
start_time = time.time()
insertsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie a dla 10**4" : czas})

my_list = losowa_lista_a(10**5)
start_time = time.time()
#insertsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie a dla 10**5" : czas})

my_list = losowa_lista_a(10**6)
start_time = time.time()
#insertsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie a dla 10**6" : czas})

#####################################################################################

os.system("clear")
print("Insert Sort dla listy wariant b")

my_list = losowa_lista_b(10**2)
start_time = time.time()
insertsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie b dla 10**2" : czas})

my_list = losowa_lista_b(10**3)
start_time = time.time()
insertsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie b dla 10**3" : czas})

my_list = losowa_lista_b(10**4)
start_time = time.time()
insertsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie b dla 10**4" : czas})

my_list = losowa_lista_b(10**5)
start_time = time.time()
#insertsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie b dla 10**5" : czas})

my_list = losowa_lista_b(10**6)
start_time = time.time()
#insertsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie b dla 10**6" : czas})

#####################################################################################

os.system("clear")
print("Insert Sort dla listy wariant c")

my_list = losowa_lista_c(10**2)
start_time = time.time()
insertsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie c dla 10**2" : czas})

my_list = losowa_lista_c(10**3)
start_time = time.time()
insertsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie c dla 10**3" : czas})

my_list = losowa_lista_c(10**4)
start_time = time.time()
insertsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie c dla 10**4" : czas})

my_list = losowa_lista_c(10**5)
start_time = time.time()
#insertsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie c dla 10**5" : czas})

my_list = losowa_lista_c(10**6)
start_time = time.time()
#insertsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie c dla 10**6" : czas})

#####################################################################################

os.system("clear")
print("Insert Sort dla listy wariant d")

my_list = losowa_lista_d(10**2)
start_time = time.time()
insertsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie d dla 10**2" : czas})

my_list = losowa_lista_d(10**3)
start_time = time.time()
insertsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie d dla 10**3" : czas})

my_list = losowa_lista_d(10**4)
start_time = time.time()
insertsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie d dla 10**4" : czas})

my_list = losowa_lista_d(10**5)
start_time = time.time()
#insertsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie d dla 10**5" : czas})

my_list = losowa_lista_d(10**6)
start_time = time.time()
#insertsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie d dla 10**6" : czas})

#####################################################################################

os.system("clear")
print("Insert Sort dla listy wariant e")

my_list = losowa_lista_e(10**2)
start_time = time.time()
insertsort(my_list, 0, 10**2 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie e dla 10**2" : czas})

my_list = losowa_lista_e(10**3)
start_time = time.time()
insertsort(my_list, 0, 10**3 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie e dla 10**3" : czas})

my_list = losowa_lista_e(10**4)
start_time = time.time()
insertsort(my_list, 0, 10**4 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie e dla 10**4" : czas})

my_list = losowa_lista_e(10**5)
start_time = time.time()
#insertsort(my_list, 0, 10**5 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie e dla 10**5" : czas})

my_list = losowa_lista_e(10**6)
start_time = time.time()
#insertsort(my_list, 0, 10**6 - 1)
czas = time.time() - start_time
wyniki["Insert Sort"].append({"Losowanie e dla 10**6" : czas})



print("Select Sort")
for x in range(len(wyniki["Select Sort"])):
	print(wyniki["Select Sort"][x])

print("\nInsert Sort")
for x in range(len(wyniki["Insert Sort"])):
	print(wyniki["Insert Sort"][x])
