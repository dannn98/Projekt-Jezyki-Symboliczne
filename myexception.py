class Error(Exception):
    pass


class GlobalException(Error):
    def __init__(self, message: str):
        self._message = message

    def printMessage(self):
        return self._message
