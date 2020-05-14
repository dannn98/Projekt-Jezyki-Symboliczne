class MyGame:

    ### Plansza i gracze
    _BOARD = [['.' for x in range(15)] for y in range(15)]
    _BLACK = 'X'
    _WHITE = 'O'

    ### Statusy gry
    _PLAY = "GRA W TOKU!"
    _DRAW = "REMIS!"
    _BLACK_WON = "CZARNE WYGRAŁY!"
    _WHITE_WON = "BIAŁE WYGRAŁY!"

    def __init__(self):
        self._status = self._PLAY
        self._currentPlayer = self._BLACK

    def getBoard(self):
        return self._BOARD

    def getStatus(self):
        return self._status

    def getCurrentPlayer(self):
        return self._currentPlayer

    def play(self, wspolrzedne: str):
        pass
        # self._BOARD[3][3] = wspolrzedne
        # self._currentPlayer = self._WHITE
