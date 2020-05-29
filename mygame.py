from myexception import *

class MyGame:

    ### Plansza i gracze
    _BOARD_SIZE = 15
    _BOARD = [['.' for x in range(15)] for y in range(15)]
    _EMPTY = '.'
    _BLACK = 'X'
    _WHITE = 'O'

    ### Statusy gry
    _PLAY = "Podaj współrzędne (np. b13)"
    _DRAW = "REMIS!"
    _BLACK_WON = "CZARNE WYGRAŁY!"
    _WHITE_WON = "BIAŁE WYGRAŁY!"

    def __init__(self):
        self._status = self._PLAY
        self._currentPlayer = self._BLACK
        self._outputInfo = self._status

    def playerMove(self, wspolrzedne: str):
        if len(wspolrzedne) > 3:
            # Exception
            raise BadCoordinatesException()
        else:
            if len(wspolrzedne) == 3:
                x = int(wspolrzedne[1:3]) - 1 ######### Tutaj wyskakuje błąd jeśli podamy literę zamiast liczbę
            elif len(wspolrzedne) == 2:
                x = int(wspolrzedne[1]) - 1 ######### Tutaj wyskakuje błąd jeśli podamy literę zamiast liczbę
            else:
                # Exception
                raise BadCoordinatesException()
            y = ord(wspolrzedne[0]) - ord('a')
            if not (0 <= x <= 14) or not (0 <= y <= 14):
                # Exception
                raise BadCoordinatesException()
            if self._BOARD[x][y] != '.':
                # Exception
                raise FieldOccupiedException()

            self._BOARD[x][y] = self._currentPlayer

    def aiMove(self):
        pass

    def statusCheck(self):
        train = 0
        win = 0
        draw = 1

        for i in range(0, 15):
            for j in range(0, 15):
                if self._BOARD[i][j] == self._currentPlayer:
                    train += 1
                    if train == 5:
                        win = 1
                        break
                elif self._BOARD[i][j] == '.':
                    train = 0
                    draw = 0
                else:
                    train = 0
            train = 0

        train = 0
        for i in range(0, 15):
            for j in range(0, 15):
                if self._BOARD[j][i] == self._currentPlayer:
                    train += 1
                    if train == 5:
                        win = 1
                        break
                else:
                    train = 0
            train = 0

        for i in range(0, 15):
            for j in range(0, i + 1):
                if self._BOARD[i - j][j] == self._currentPlayer:
                    train += 1
                    if train == 5:
                        win = 1
                        break
                else:
                    train = 0
            train = 0

        for j in range(1, 15):
            for i in range(0, 15 - j):
                if self._BOARD[14 - i][j + i] == self._currentPlayer:
                    train += 1
                    if train == 5:
                        win = 1
                        break
                else:
                    train = 0
            train = 0

        for i in range(0, 15):
            for j in range(0, i + 1):
                if self._BOARD[i - j][14 - j] == self._currentPlayer:
                    train += 1
                    if train == 5:
                        win = 1
                        break
                else:
                    train = 0
            train = 0

        for j in range(0, 14):
            for i in range(0, j + 1):
                if self._BOARD[14 - i][j - i] == self._currentPlayer:
                    train += 1
                    if train == 5:
                        win = 1
                        break
                else:
                    train = 0
            train = 0

        if win == 1:
            if self._currentPlayer == self._BLACK:
                self._status = self._BLACK_WON
            else:
                self._status = self._WHITE_WON
        elif draw == 1:
            self._status = self._DRAW

    def playerSwap(self):
        if self._currentPlayer == self._BLACK:
            self._currentPlayer = self._WHITE
        else:
            self._currentPlayer = self._BLACK

    def newGame(self):
        self._currentPlayer = self._BLACK
        self._outputInfo = self._PLAY
        self._status = self._PLAY
        self._BOARD = [['.' for x in range(15)] for y in range(15)]

    def getBoardSize(self):
        return self._BOARD_SIZE

    def getBoard(self):
        return self._BOARD

    def getStatus(self):
        return self._status

    def getCurrentPlayer(self):
        return self._currentPlayer

    def getOutputInfo(self):
        return self._outputInfo

    def play(self, wspolrzedne: str):
        try:
            if self.getStatus() != self._PLAY:
                # Exception
                raise GameOverException()
            self.playerMove(wspolrzedne)
            self.statusCheck()
            ### Zakomentować jeśli PvP
            if self.getStatus() != self._PLAY:
                # Exception
                raise GameOverException()
            self.playerSwap()
            self.aiMove()
            self.statusCheck()
            ###
            self.playerSwap()
        except BadCoordinatesException as e:
            self._outputInfo = f'{e.printMessage()} {self.getStatus()}'
        except FieldOccupiedException as e:
            self._outputInfo = f'{e.printMessage()} {self.getStatus()}'
        except GameOverException as e:
            self._outputInfo = f'{e.printMessage()} {self.getStatus()}'
        except UndefinedException as e:
            self._outputInfo = f'{e.printMessage()} {self.getStatus()}'
        else:
            self._outputInfo = self.getStatus()
