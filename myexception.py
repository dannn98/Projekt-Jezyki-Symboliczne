class Error(Exception):
        pass


class UndefinedException(Error):
    def __init__(self, message: str):
        self._message = message

    def printMessage(self):
        return self._message


class BadCoordinatesException(Error):
    def __init__(self):
        self._message = "Podano złe współrzędne!"

    def printMessage(self):
        return self._message


class FieldOccupiedException(Error):
    def __init__(self):
        self._message = "Podane pole jest zajęte!"

    def printMessage(self):
        return self._message


class GameOverException(Error):
    def __init__(self):
        pass
