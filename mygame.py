"""Moduł zawierający klasę MyGame do obsługi logiki gry"""
import myexception as ex


class MyGame:
    """Klasa obsługująca logikę gry"""
    # Plansza i gracze
    _BOARD_SIZE = 15
    _BOARD = [['.' for x in range(15)] for y in range(15)]
    _EMPTY = '.'
    _BLACK = 'X'
    _WHITE = 'O'

    # Statusy gry
    GOING_ON, VICTORY, DRAW = range(3)
    _PLAY = "Podaj współrzędne (np. b13)"
    _DRAW = "REMIS!"
    _BLACK_WON = "CZARNE WYGRAŁY!"
    _WHITE_WON = "BIAŁE WYGRAŁY!"

    def __init__(self):
        self._status = self._PLAY
        self._current_player = self._BLACK
        self._output_info = self._status

    def player_move(self, wspolrzedne: str):
        """Funkcja wprowadza współrzędne podane przez gracza na planszę"""
        if len(wspolrzedne) > 3:
            # Exception
            raise ex.BadCoordinatesException()

        if len(wspolrzedne) == 3:
            # Tutaj wyskakuje błąd jeśli podamy literę zamiast liczbę
            x_coordinate = int(wspolrzedne[1:3]) - 1
        elif len(wspolrzedne) == 2:
            # Tutaj wyskakuje błąd jeśli podamy literę zamiast liczbę
            x_coordinate = int(wspolrzedne[1]) - 1
        else:
            # Exception
            raise ex.BadCoordinatesException()
        y_coordinate = ord(wspolrzedne[0]) - ord('a')
        if not (0 <= x_coordinate <= 14) or not (0 <= y_coordinate <= 14):
            # Exception
            raise ex.BadCoordinatesException()
        if self._BOARD[x_coordinate][y_coordinate] != '.':
            # Exception
            raise ex.FieldOccupiedException()

        self._BOARD[x_coordinate][y_coordinate] = self._current_player

    def ai_move(self):
        """Funkcja AI gry"""

    def check_method_1(self):
        """Funkcja sprawdza w poziomie"""
        train = 0
        draw = 1
        for i in range(0, 15):
            for j in range(0, 15):
                if self._BOARD[i][j] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                elif self._BOARD[i][j] == self._EMPTY:
                    train = 0
                    draw = 0
                else:
                    train = 0
            train = 0
        if draw:
            return self.DRAW
        else:
            return self.GOING_ON

    def check_method_2(self):
        """Funkcja sprawdza w pionie"""
        train = 0
        for i in range(0, 15):
            for j in range(0, 15):
                if self._BOARD[j][i] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def check_method_3(self):
        """Funkcja sprawdza na skos"""
        train = 0
        for i in range(0, 15):
            for j in range(0, i + 1):
                if self._BOARD[i - j][j] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def check_method_4(self):
        """Funkcja sprawdza na skos"""
        train = 0
        for j in range(1, 15):
            for i in range(0, 15 - j):
                if self._BOARD[14 - i][j + i] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def check_method_5(self):
        """Funkcja sprawdza na skos"""
        train = 0
        for i in range(0, 15):
            for j in range(0, i + 1):
                if self._BOARD[i - j][14 - j] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def check_method_6(self):
        """Funkcja sprawdza na skos"""
        train = 0
        for j in range(0, 14):
            for i in range(0, j + 1):
                if self._BOARD[14 - i][j - i] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def status_check(self):
        """
        Funkcja sprawdzająca stan planszy/gry
        (Wygrana/Remis/Nadal trwa)
        """
        game_status = self.check_method_1()
        if game_status == self.GOING_ON:
            game_status = self.check_method_2()
            if game_status == self.GOING_ON:
                game_status = self.check_method_3()
                if game_status == self.GOING_ON:
                    game_status = self.check_method_4()
                    if game_status == self.GOING_ON:
                        game_status = self.check_method_5()
                        if game_status == self.GOING_ON:
                            game_status = self.check_method_6()

        if game_status == self.VICTORY:
            if self._current_player == self._BLACK:
                self._status = self._BLACK_WON
            else:
                self._status = self._WHITE_WON
        elif game_status == self.DRAW:
            self._status = self._DRAW

    def player_swap(self):
        """Zamiana aktualnego gracza"""
        if self._current_player == self._BLACK:
            self._current_player = self._WHITE
        else:
            self._current_player = self._BLACK

    def new_game(self):
        """Powrót do startowego stanu gry"""
        self._current_player = self._BLACK
        self._output_info = self._PLAY
        self._status = self._PLAY
        self._BOARD = [[self._EMPTY for x in range(self._BOARD_SIZE)]
                       for y in range(self._BOARD_SIZE)]

    def get_board_size(self):
        """Zwraca rozmiar planszy"""
        return self._BOARD_SIZE

    def get_board(self):
        """Zwraca planszę"""
        return self._BOARD

    def get_status(self):
        """Zwraca status gry"""
        return self._status

    def get_current_player(self):
        """Zwraca aktualnego gracza"""
        return self._current_player

    def get_output_info(self):
        """Zwraca informację z logiki gry"""
        return self._output_info

    def play(self, wspolrzedne: str):
        """Główna funkcja gry"""
        try:
            if self.get_status() != self._PLAY:
                # Exception
                raise ex.GameOverException()
            self.player_move(wspolrzedne)
            self.status_check()
            # Zakomentować jeśli PvP
            if self.get_status() != self._PLAY:
                # Exception
                raise ex.GameOverException()
            self.player_swap()
            self.ai_move()
            self.status_check()
            #
            self.player_swap()
        except ex.BadCoordinatesException as err:
            self._output_info = f'{err.print_message()} {self.get_status()}'
        except ex.FieldOccupiedException as err:
            self._output_info = f'{err.print_message()} {self.get_status()}'
        except ex.GameOverException as err:
            self._output_info = f'{err.print_message()} {self.get_status()}'
        except ex.UndefinedException as err:
            self._output_info = f'{err.print_message()} {self.get_status()}'
        else:
            self._output_info = self.get_status()
