import unittest
from unittest.mock import patch

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

class TestPowersLoop(unittest.TestCase):

    def test_correct_inputs(self):
        inputs = ["2", "3", "stop"]
        with patch("builtins.input", side_effect=inputs):
            wynik = powers_loop()
        self.assertEqual(wynik, [(2.0, 8.0), (3.0, 27.0)])

    def test_incorrect_input(self):
        inputs = ["abc", "2", "stop"]
        with patch("builtins.input", side_effect=inputs):
            wynik = powers_loop()
        self.assertEqual(wynik, [(2.0, 8.0)])

    def test_mixed_inputs(self):
        inputs = ["1.5", "xyz", "-2", "stop"]
        with patch("builtins.input", side_effect=inputs):
            wynik = powers_loop()
        self.assertEqual(wynik, [(1.5, 3.375), (-2.0, -8.0)])

if __name__ == "__main__":
    unittest.main()