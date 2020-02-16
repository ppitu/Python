### Drzewo AVL
  
**Drzeno AVL** - jest to zrównoważone binarne drzewo poszukiwań (BST), w którym wysokość lewego i
prawego poddrzewa każdego węzła różni się co najwyżej o jeden.
  
## Operacje
  
Algorytmy podstawowych operacji na drzewie AVL przypominają te z binarnych drzew poszukiwań, ale sa
 poprzedzane lub następują po niech jedna lub wiecej rotacji. Koszt każdej operacji to O(log n)
  
# Wstawanie
  
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
