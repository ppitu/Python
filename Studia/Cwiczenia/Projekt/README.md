# Drzewo AVL
  
**Drzeno AVL** - jest to zrównoważone binarne drzewo poszukiwań (BST), w którym wysokość lewego i
prawego poddrzewa każdego węzła różni się co najwyżej o jeden.
  
## Operacje
  
Algorytmy podstawowych operacji na drzewie AVL przypominają te z binarnych drzew poszukiwań, ale sa
 poprzedzane lub następują po niech jedna lub wiecej rotacji. Koszt każdej operacji to O(log n)
  
### Wstawanie
  
Wstanianie do drzewa AVL wyglada tak samo, najpierw przeszukujemy drzewo w celu odszukania mejsca 
wstawienia elementu, nastepnie wstawiamy ten element. Po wstawieniu element następuje sprawdzenie 
czy drzewo jest zrownowazone tzn. czy wysokość pomiędzy prawym a lewym poddrzewem są równe: -1, 0, 1
 jeżeli mają wartości inne niż podane powyżej następuję tak zwana rotacja drzewa. Mamy następujące 
rotacje:  
- Rotacja pojedyncza **LL** (ang. Left-Left)  
- Roracja pojedyncza **RR** (ang. Right-Right)  
- Rotacja podwójna **RL** (ang. Right-Left)  
- Rotacja podwójna **LR** (ang. Left-Right)  
  
**Rotacja RR**
  
W rotacji RR uczestniczą węzły A i B. Węzeł B zajmuje miejsce węzła A, węzeł A staje sie lewym synem
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
  
Usuwanie elementu z drzewa AVL odbywa się tak samo jak w przypadku drzewa BST (szukamy elementu do usuniecia a następnie go usuwamy zachowując wszystkie własniści drzewa BST) to wykonanej operacji 
usuwania sprawdzamy czu drzewo jest zrównoważone, jeśli nie wykonujemy rotacji jak w przypadku wstawiania.  
  
### Opis projektu
  
Moje drzewa AVL sklada sie z dwóch klas Node i AVLTree, które odpwiadają za następujące funkcję:  
- Node za wezły drzewa  
- AVLTree za operacje na drzewie  
  
Dodatkowo drzewa zawiera dwie funnkcje wypisujące drzewa:  
- PrintTree - funkcja ta wypisuje drzewo w postaci drzewa (wizualizuje wygląd drzewa)    
- preOreder - funkcja wypisuje elementy drzewa w przejsciu preOrder przez drzewo  

Impplementacja posiada również funkcję sizeTree, która zwraca ile elementów zawiera drzewo.
