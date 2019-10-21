x = 2 ; y = 3 ;
if (x > y):
    result = x;
else:
    result = y;
#powyzszy kod jest poprawny zarowno w python3 jak i python2

#for i in "qwerty": if ord(i) < 100: print i
#powyzszy kod jest niepoprawny

for i in "axby": print ord(i) if ord(i) < 100 else i
#powyzszy kod jest poprawny w python2 ale nie w python3 poniewaz nie ma nawiasow przy print
