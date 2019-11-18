Rownania z dwiem niewiadomymi zawieraja dwie zmienne, zwykle oznaczone jako x i y (moga to byc dowolne litery z alfabetu). Zazwyczaj sa formatu:
ax + by + c = 0
Gdzie a, b i c to wspolczynniki liczbowe.

Rozwiazaniem takie rownania sa:
Gdy a = 0 i b != 0:
	Otrzymujemy rownanie postacie 0x + by + c = 0 stad otrzymujemy, że nie zalezy od x. Stąd y = -c/b. Zatem rozwiazaniem tego rownania jest kazda para liczb postaci (0, -c/b) czyli jest to prosta przechodzaca przez punkt (0, -c/b).
Moje rozwiazanie zwraca taki punkt.

Gdy a != 0 i b = 0:
	Sytuacja jest analogiczna a rozwiazaniem rownania jest kazda para liczb postac (-c/a, 0)
Moje rowiazanie zwraca taki punkt.

Gdy a != 0 i b != 0:
	Wtedy rozwiazanie rownania jest kazda para liczb postaci (r, -a/b*r - c.b) gdzie r jest dowolna liczba naturalna. 
Jest to zarazem prosta przechodzaca przez punkty (0, -c/b) oraz (-c/a, 0) i takie punkty zwraca moja funkcja.
