# Python-zestaw-3
Plik zestaw_3_zadania zawiera wszystkie zadania z zestawu oprócz opisanych poniżej zadań 3.1 i 3.2 oraz zadania 3.7. Plik zad3_4 zawiera zadanie 3.4 i jego test w bloku main.
## Zadanie 3.1 - Poprawność składniowa 
x = 2; y = 3;  
if (x > y):  
    result = x;  
else:  
    result = y;  
for i in "axby": if ord(i) < 100: print(i)  
for i in "axby": print(ord(i) if ord(i) < 100 else i)  
Podany kod nie jest poprawny składniowo. Wyrażenie - for i in "axby": if ord(i) < 100: print(i) - nie jest poprawne składniowo, python nie pozwala na użycie if w tej postaci w jednej linii z for. W wyrażeniu - for i in "axby": print(ord(i) if ord(i) < 100 else i) - print() jest funkcją, a wyrażenie warunkowe (ord(i) if ord(i) < 100 else i) jest poprawne jako argument funkcji, python pozwala na takie jednoliniowe wywołanie for, zatem cała ta część jest poprawna.

## Zadanie 3.2 - co jest złego w kodzie
L = [3, 5, 4] ; L = L.sort() - metoda list.sort() nie zwraca posortowanej listy tylko modyfikuje ją w miejscu, dlatego przypisanie L=L.sort() sprawi że L przyjmie wartość None.   
x, y = 1, 2, 3  - po lewej stronie przypisanie są 2 zmienne, a po prawej 3 wartości, python nie będzie wiedział jak to dopasować.  
X = 1, 2, 3 ; X[1] = 4  - wyrażenie X = 1, 2, 3 tworzy krotkę, a krotka jest niemodyfikowalna, dlatego nie możemy zmieniać jej elementów przez indeksowanie.   
X = [1, 2, 3] ; X[3] = 4  - indeksy w pythonie zaczynają się od 0. Dla listy [1, 2, 3] mamy więc indeksy 0, 1, 2. Indeks 3 jest out of range.  
X = "abc" ; X.append("d")  - ciągi znaków są niemodyfikowalne i nie mają metody append.  
L = list(map(pow, range(8)))  - funkcja pow() wymaga 2 argumentów, ale map(pow, range(8)) przekazuje tylko 1.  

