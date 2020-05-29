class Error(Exception):
    def __init__(self, message: str):
        self._message = message

    def printMessage(self):
        return self._message


class UndefinedException(Error):
    pass


class BadCoordinatesException(Error):
    def __init__(self):
        super().__init__("Podano złe współrzędne!")


class FieldOccupiedException(Error):
    def __init__(self):
        super().__init__("Podane pole jest zajęte!")


class GameOverException(Error):
    def __init__(self):
        super().__init__("KONIEC GRY!")
