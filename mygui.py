import string
from tkinter import *
from myexception import *

class MyGUI:
    def __init__(self, master, game):
        self._master = master
        master.title("Projekt Gomoku")

        # Zmienne tekstowe używane w Label aby można było je odświeżać
        self._playerStr = StringVar()
        self._boardStr = StringVar()
        self._infoStr = StringVar()
        # Ustawienie zmiennych tekstowych
        self._playerStr.set(f"Tura gracza: {game.getCurrentPlayer()}")
        self._boardStr.set(self.printBoard(game))
        self._infoStr.set(game.getOutputInfo())

        self._player = Label(master, textvariable=self._playerStr)
        self._player.grid(row=0, columnspan=4)

        self._board = Label(master, textvariable=self._boardStr)
        self._board.grid(row=1, columnspan=4)

        self._info = Label(master, textvariable=self._infoStr)
        self._info.grid(row=2, columnspan=4)

        self._newGame = Button(master, text="Nowa gra", command=lambda: self.clickNewGame(game))
        self._newGame.grid(sticky=E, row=3, column=0, padx=5, pady=5)

        self._input = Entry(master)
        self._input.grid(sticky=E, row=3, column=1, padx=5, pady=5)

        self._submit = Button(master, text="Zatwierdź", command=lambda: self.clickSubmit(game))
        self._submit.grid(sticky=W, row=3, column=2, padx=5, pady=5)

        self._exit = Button(master, text="Wyjście", command=lambda: exit(0))
        self._exit.grid(sticky=W, row=3, column=3, padx=5, pady=5)

    def refresh(self, game):
        self._playerStr.set(f"Tura gracza: {game.getCurrentPlayer()}")
        self._boardStr.set(self.printBoard(game))
        self._infoStr.set(game.getOutputInfo())
        self._input.delete(0, 'end')

    def printBoard(self, game):
        strBoard = '\n'
        board = game.getBoard()
        boardSize = game.getBoardSize()
        lista = []
        for i in range(boardSize + 1):
            if i == 0:
                tmp = ['\t#']
                tmp += string.ascii_lowercase[:boardSize]
                tmp.append('\t')
                lista.append('\t'.join(tmp))
            else:
                tmp = [f'\t{i}']
                tmp += board[i - 1][:]
                tmp.append('\t')
                lista.append('\t'.join(tmp))

        strBoard += '\n\n\n'.join(lista)
        strBoard += '\n'

        return strBoard

    def clickSubmit(self, game):
        game.play(self._input.get())
        self.refresh(game)

    def clickNewGame(self, game):
        game.newGame()
        self.refresh(game)
