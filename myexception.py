"""Moduł zawierający klasy wyjątków"""

class Error(Exception):
    """Klasa bazowa dla innych klas wyjątków"""
    def __init__(self, message: str):
        self._message = message

    def print_message(self):
        """Metoda wypisująca treść wiadomości wyjątku"""
        return self._message


class UndefinedException(Error):
    """Niezdefiniowany wyjątek"""


class BadCoordinatesException(Error):
    """Wprowadzenie błędnych współrzędnych"""
    def __init__(self):
        super().__init__("Podano złe współrzędne!")


class FieldOccupiedException(Error):
    """Wprowadzenie zajętych współrzędnych"""
    def __init__(self):
        super().__init__("Podane pole jest zajęte!")


class GameOverException(Error):
    """Koniec gry"""
    def __init__(self):
        super().__init__("KONIEC GRY!")
