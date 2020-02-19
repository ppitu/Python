# Drzewo AVL

**Autro: Piotr Chmura**  
**Data oddania projektu: 18.02.2019**  
  
**Drzeno AVL** - jest to zrównoważone binarne drzewo poszukiwań (BST), w którym wysokość lewego i
prawego poddrzewa każdego węzła różni się co najwyżej o jeden.
  
## Operacje
  
Algorytmy podstawowych operacji na drzewie AVL przypominają te z binarnych drzew poszukiwań, ale sa
 poprzedzane lub następują po niech jedna lub wiecej rotacji. Koszt każdej operacji to O(log n)
  
### Wstawianie
  
Wstanianie do drzewa AVL wygląda tak samo jak to BST, najpierw przeszukujemy drzewo w celu odszukania mejsca 
wstawienia elementu, nastepnie wstawiamy ten element. Po wstawieniu elementu następuje sprawdzenie 
czy drzewo jest zrównoważone tzn. czy wysokość pomiędzy prawym a lewym poddrzewem są równe: -1, 0, 1
 jeżeli mają wartości inne niż podane powyżej następuję tak zwana rotacja drzewa. Mamy następujące 
rotacje:  
- Rotacja pojedyncza **LL** (ang. Left-Left)  
- Roracja pojedyncza **RR** (ang. Right-Right)  
- Rotacja podwójna **RL** (ang. Right-Left)  
- Rotacja podwójna **LR** (ang. Left-Right)  
  
**Rotacja RR**
  
W rotacji RR uczestniczą węzły A i B. Węzeł B zajmuje miejsce węzła A, węzeł A staje się lewym synem
 węzła B. Lewy syn węzła B (BL) staje sie prawym synem węzla A.
  
**Rotacja LL**
  
Rotacja LL jest lustrzanym odbiciem rotacji RR. W rotacji uczestniczą dwa węzły A i B. Węzeł B 
zajmuje miejsce węzła A, węzeł A staje się prawym synem węzła B.
  
**Rotacja RL**
  
Rotacja RL jest złożeniem rotacji LL i rotacji RR. Pierwza rotacja LL sprowadza gałąź drzewa do 
postaci dogodnej dla następnej rotacji RR.
  
**Rotacja LR**
  
Rotacja LR jest złożeniem rotacji RR i LL. Jest lustrzanym odbiciem rotacji RL.
  
### Usuwanie
  
Usuwanie elementu z drzewa AVL odbywa się tak samo jak w przypadku drzewa BST (szukamy elementu do usuniecia a następnie go usuwamy zachowując wszystkie własniści drzewa BST) po wykonanej operacji 
usuwania sprawdzamy czy drzewo jest zrównoważone, jeśli nie wykonujemy rotacje jak w przypadku wstawiania.  
  
### Opis projektu
  
Moje drzewa AVL sklada sie z dwóch klas Node i AVLTree, które odpwiadają za następujące funkcję:  
- Node za wezły drzewa  
- AVLTree za operacje na drzewie  
  
Dodatkowo drzewo zawiera dwie funnkcje wypisujące drzewa:  
- PrintTree - funkcja ta wypisuje drzewo w postaci drzewa (wizualizuje wygląd drzewa)    
- preOreder - funkcja wypisuje elementy drzewa w przejsciu preOrder przez drzewo  

Funkcja is_avl() sprawdza czy drzewa jest w postaci avl wykorzystujac roznice wysokosci prawego i lewego poddrzewa  

Implementacja posiada również funkcję sizeTree, która zwraca ile elementów, które zawiera drzewo.

Źródła:  
https://eduinf.waw.pl/inf/alg/001_search/0108.php  
https://pl.wikipedia.org/wiki/Drzewo_AVL  

