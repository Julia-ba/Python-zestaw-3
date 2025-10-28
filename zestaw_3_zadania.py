"""
Zestaw zadan 3 - bez zadania 3.7
testy do zadan (oprocz testu do zadania 3.4 - ten  oddzielnie w pliku zad3_4.py)  znajduja sie w bloku main
funkcje roman2int, roman2int_ver_2, roman2int_ver_3 spelniaja to samo zadanie,
ale pokazuja rozne sposoby tworzenia slownika
"""
def numbers_not_divisible_by_3(n=30):
    """
    Zwraca liste liczb od 0 do n wlacznie, ktore nie sa podzielne przez 3.
    """
    return [i for i in range(n+1) if i % 3 != 0]

def powers_loop():
    """
    Pobiera liczby rzeczywiste od uzytkownika i wypisuje je wraz z ich szescianem.
    Zatrzymanie po wpisaniu 'stop'.
    """
    result = []
    while True:
        s = input("Podaj liczbe (lub stop aby zakonczyc): ")
        if s.lower() == 'stop':
            break
        try:
            x = float(s)
            result.append((x, x**3))
        except ValueError:
            print("Niepoprawne dane wpisz liczbe lub  napis 'stop' ")
            continue
    return result

def draw_ruler(length):
    """
    Tworzy string przedstawiajacy miarke o zadanej dlugosci.
    """
    top = "|...." * length + "|\n"
    numbers = ""
    for i in range(length + 1):
        numbers += str(i)
        if i < length:
            numbers += " " * (5 - len(str(i + 1)))
    return top + numbers

def draw_rectangle(row, col):
    """
    Tworzy prostokat z malych kratek o podanej liczbie wierszy i kolumn.
    """
    line_ver = "|" + "   |"*col + "\n"
    line_hor = "+" + "---+"*col + "\n"
    rec = (line_hor + line_ver) * row + line_hor
    return rec

def common_union(seq1, seq2):
    """
     Zwraca krotke dwoch list:
     - elementy wspolne (bez powtorzen)
     - wszystkie elementy (bez powtorzen)
    """
    set1, set2 = set(seq1), set(seq2)
    return list(set1 & set2), list(set1 | set2)

def sum_of_sequences(seq_list):
    """
    Zwraca liste sum elementow kazdej sekwencji z listy sekwencji.
    """
    return [sum(seq) for seq in seq_list]

def roman2int(roman):
    """
    Funkcja zamieniajaca liczby rzymskie na arabskie.
    """
    roman_dict = {'I':1, 'V':5, 'X':10, 'L':50,
                  'C':100, 'D':500, 'M':1000}
    total = 0
    prev = 0
    for i in reversed(roman):
        val = roman_dict[i]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

def roman2int_ver_2(roman):
    """
    Funkcja zamieniajaca liczby rzymskie na arabskie.
    """
    roman_dict = dict([
        ('I', 1), ('V', 5), ('X', 10),
        ('L', 50), ('C', 100),
        ('D', 500), ('M', 1000)
    ])
    total = 0
    prev = 0
    for i in reversed(roman):
        val = roman_dict[i]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

def roman2int_ver_3(roman):
    """
    Funkcja zamieniajaca liczby rzymskie na arabskie.
    """
    letters = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    values = [1, 5, 10, 50, 100, 500, 1000]
    roman_dict = dict(zip(letters, values))
    total = 0
    prev = 0
    for i in reversed(roman):
        val = roman_dict[i]
        if val < prev:
            total -= val
        else:
            total += val
        prev = val
    return total

if __name__ == "__main__":
    # 3.3
    assert numbers_not_divisible_by_3(10) == [1, 2, 4, 5, 7, 8, 10]

    # 3.5
    ruler_test = draw_ruler(8)
    print("Wynik draw_ruler(8):")
    print(ruler_test)
    lines = ruler_test.split('\n')
    first_line = lines[0]
    numbers_line = lines[1]
    #liczba kresek o 1 wieksza niz dlugosc miarki
    assert first_line.count('|') == 9
    #wszystkie liczby od 0 do 8 powinny wystepowac w dolnej linii
    for i in range(9):
        assert str(i) in numbers_line
    #ostatnia liczba 8 powinna sie znajdowac pod ostatnia kreska
    last_number = "8"
    ind_last_bar = first_line.rindex('|')
    assert numbers_line[ind_last_bar - len(last_number) + 1: ind_last_bar + 1] == last_number

    # 3.6
    rect_test = draw_rectangle(3, 5)
    print("Wynik draw_rectangle(3, 5):")
    print(rect_test)
    # W prostokacie o 3 wierszach i 5 kolumnach
    # powinno byc (3 + 1) * (5 + 1) znakow "+"
    assert rect_test.count("+") == (3 + 1) * (5 + 1)
    # Rysunek powinien zaczynac się od "+" (gorny lewy róg)
    # i konczyc się na "+\n" (dolny prawy rog)
    assert rect_test.startswith("+") and rect_test.endswith("+\n")

    # 3.8
    common, union = common_union([1, 2, 3, 4], [3, 4, 5, 6])
    assert set(common) == {3, 4}
    assert set(union) == {1, 2, 3, 4, 5, 6}

    # 3.9
    sums = sum_of_sequences([[], [4], (1, 2), [3, 4], (5, 6, 7)])
    assert sums == [0, 4, 3, 7, 18]

    # 3.10
    assert roman2int("IX") == 9
    assert roman2int("MCMXCIV") == 1994
    assert roman2int_ver_2("III") == 3
    assert roman2int_ver_2("MCMXCIV") == 1994
    assert roman2int_ver_3("II") == 2
    assert roman2int_ver_3("LVIII") == 58

    print("All tests passed successfully")




