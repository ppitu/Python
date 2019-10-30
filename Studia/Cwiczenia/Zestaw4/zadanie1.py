"""X = "qwerty"

def func():
    print X

func()

#W python3 powyzszy kod nie zadziala ze wzgledu na brak nawiasow przy print
#W python2 kod wypisze qwerty
"""
"""
X = "qwerty"

def func():
    X = "abc"

func()
print X
#Znow brak nawiasow przy print wiec w python3 nie zadziala
#W python dwa wypisze qwerty poniewaz w funkcji func() przypisujemy abc do zmiennej lokalnej
"""
X = "qwerty"

def func():
    global X
    X = "abc"

func()
print X
#wypisze abc poniewaz w funkcji uzywamy global X przez co dzialmy na zmiennej globalnej a nie lokalnej
