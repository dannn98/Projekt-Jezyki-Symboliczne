import string
from tkinter import *
# from myexception import *


class MyGUI:
    def __init__(self, master, game):
        self._master = master
        master.title("Projekt Gomoku")

        # Zmienne tekstowe używane w Label aby można było je odświeżać
        self._player_str = StringVar()
        self._board_str = StringVar()
        self._info_str = StringVar()
        # Ustawienie zmiennych tekstowych
        self._player_str.set(f"Tura gracza: {game.get_current_player()}")
        self._board_str.set(self.print_board(game))
        self._info_str.set(game.get_output_info())

        self._player = Label(master, textvariable=self._player_str)
        self._player.grid(row=0, columnspan=4)

        self._board = Label(master, textvariable=self._board_str)
        self._board.grid(row=1, columnspan=4)

        self._info = Label(master, textvariable=self._info_str)
        self._info.grid(row=2, columnspan=4)

        self._new_game = Button(master, text="Nowa gra", command=lambda: self.click_new_game(game))
        self._new_game.grid(sticky=E, row=3, column=0, padx=5, pady=5)

        self._input = Entry(master)
        self._input.grid(sticky=E, row=3, column=1, padx=5, pady=5)

        self._submit = Button(master, text="Zatwierdź", command=lambda: self.click_submit(game))
        self._submit.grid(sticky=W, row=3, column=2, padx=5, pady=5)

        self._exit = Button(master, text="Wyjście", command=lambda: exit(0))
        self._exit.grid(sticky=W, row=3, column=3, padx=5, pady=5)

    def refresh(self, game):
        self._player_str.set(f"Tura gracza: {game.get_current_player()}")
        self._board_str.set(self.print_board(game))
        self._info_str.set(game.get_output_info())
        self._input.delete(0, 'end')

    def print_board(self, game):
        str_board = '\n'
        board = game.get_board()
        board_size = game.get_board_size()
        lista = []
        for i in range(board_size + 1):
            if i == 0:
                tmp = ['\t#']
                tmp += string.ascii_lowercase[:board_size]
                tmp.append('\t')
                lista.append('\t'.join(tmp))
            else:
                tmp = [f'\t{i}']
                tmp += board[i - 1][:]
                tmp.append('\t')
                lista.append('\t'.join(tmp))

        str_board += '\n\n\n'.join(lista)
        str_board += '\n'

        return str_board

    def click_submit(self, game):
        game.play(self._input.get())
        self.refresh(game)

    def click_new_game(self, game):
        game.new_game()
        self.refresh(game)
