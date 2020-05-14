from tkinter import *

class MyGUI:
    def __init__(self, master, game):
        self._master = master
        master.title("Projekt Gomoku")

        self._player = Label(master, text=f"Tura gracza: {game.getCurrentPlayer()}")
        self._player.grid(row=0, columnspan=2)

        self._board = Label(master, text=self.printBoard(game))
        self._board.grid(row=1, columnspan=2)

        self._info = Label(master, text="Podaj współrzędne (np. b13)")
        self._info.grid(row=2, columnspan=2)

        self._input = Entry(master)
        self._input.grid(sticky=E, row=3, column=0, padx=5, pady=5)

        self.submit = Button(master, text="Zatwierdź", command=lambda: self.onClick(game))
        self.submit.grid(sticky=W, row=3, column=1, padx=5, pady=5)

    def refresh(self, game):
        self._player = Label(self._master, text=f"Tura gracza: {game.getCurrentPlayer()}")
        self._player.grid(row=0, columnspan=2)

        self._board = Label(self._master, text=self.printBoard(game))
        self._board.grid(row=1, columnspan=2)

        self._info = Label(self._master, text="Podaj współrzędne (np. b13)")
        self._info.grid(row=2, columnspan=2)

        self._input = Entry(self._master)
        self._input.grid(sticky=E, row=3, column=0, padx=5, pady=5)

        self.submit = Button(self._master, text="Zatwierdź", command=lambda: self.onClick(game))
        self.submit.grid(sticky=W, row=3, column=1, padx=5, pady=5)

    def printBoard(self, game):
        strBoard = '\n'
        board = game.getBoard()
        for i in range(16):
            if i == 0:
                strBoard += '\t' + '#'
                for j in range(97, 112):
                    strBoard += '\t' + chr(j)
            else:
                for j in range(16):
                    if j == 0:
                        strBoard += '\t' + str(i)
                    else:
                        strBoard += '\t' + board[i-1][j-1]
            if i < 15:
                strBoard += '\t\n\n\n'
            else:
                strBoard += '\t\n'

        return strBoard

    def onClick(self, game):
        game.play(self._input.get())
        self.refresh(game)
