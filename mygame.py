"""Moduł zawierający klasę MyGame do obsługi logiki gry."""
import copy
import myexception as ex


class MyGame:
    """Klasa obsługująca logikę gry."""
    # Plansza i gracze
    _BOARD_SIZE = 15
    _BOARD = [['.' for x in range(15)] for y in range(15)]
    _EMPTY = '.'
    _BLACK = 'X'
    _WHITE = 'O'
    _GREEN = 'M'

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
        """Funkcja wprowadza współrzędne podane przez gracza na planszę."""
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
        if not (0 <= x_coordinate < self._BOARD_SIZE) or not (0 <= y_coordinate < self._BOARD_SIZE):
            # Exception
            raise ex.BadCoordinatesException()
        if self._BOARD[x_coordinate][y_coordinate] != '.':
            # Exception
            raise ex.FieldOccupiedException()

        self._BOARD[x_coordinate][y_coordinate] = self._current_player

    def ai_move_table(self):
        """Funkcja do przygotowania tablicy dla funkcji minmax."""
        move_table = [[self._EMPTY for x in range(15)] for y in range(15)]
        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if self._BOARD[i][j] != self._EMPTY:
                    move_table[i][j] = self._BOARD[i][j]
                    if i != 0:
                        if j != 0:
                            if self._BOARD[i - 1][j - 1] == self._EMPTY:
                                move_table[i - 1][j - 1] = self._GREEN
                        if self._BOARD[i - 1][j] == self._EMPTY:
                            move_table[i - 1][j] = self._GREEN
                        if j != self._BOARD_SIZE - 1:
                            if self._BOARD[i - 1][j + 1] == self._EMPTY:
                                move_table[i - 1][j + 1] = self._GREEN
                    if j != 0:
                        if self._BOARD[i][j - 1] == self._EMPTY:
                            move_table[i][j - 1] = self._GREEN
                    if j != self._BOARD_SIZE - 1:
                        if self._BOARD[i][j + 1] == self._EMPTY:
                            move_table[i][j + 1] = self._GREEN
                    if i != self._BOARD_SIZE - 1:
                        if j != 0:
                            if self._BOARD[i + 1][j - 1] == self._EMPTY:
                                move_table[i + 1][j - 1] = self._GREEN
                        if self._BOARD[i + 1][j] == self._EMPTY:
                            move_table[i + 1][j] = self._GREEN
                        if j != self._BOARD_SIZE - 1:
                            if self._BOARD[i + 1][j + 1] == self._EMPTY:
                                move_table[i + 1][j + 1] = self._GREEN

        return move_table

    def evaluation(self, move_table: []):
        """Funkcja oceniająca ruch."""
        black_best = 0
        white_best = 0
        again = False
        train = 0

        # BLACK

        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if move_table[i][j] == self._BLACK:
                    train += 1
                elif move_table[i][j] == self._GREEN:
                    train += 0.5
                elif move_table[i][j] == self._WHITE:
                    if again:
                        if train < 4.5:
                            train = 0
                        else:
                            black_best = 5
                    else:
                        again = True
                        if train > black_best:
                            black_best = train
                        train = 0
                else:
                    if train > black_best:
                        black_best = train
                    train = 0
            if again:
                if train >= 4.5:
                    black_best = 5
            else:
                if train > black_best:
                    black_best = train
            again = False
            train = 0

        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if move_table[j][i] == self._BLACK:
                    train += 1
                elif move_table[j][i] == self._GREEN:
                    train += 0.5
                elif move_table[j][i] == self._WHITE:
                    if again:
                        if train < 4.5:
                            train = 0
                        else:
                            black_best = 5
                    else:
                        again = True
                        if train > black_best:
                            black_best = train
                        train = 0
                else:
                    if train > black_best:
                        black_best = train
                    train = 0
            if again:
                if train >= 4.5:
                    black_best = 5
            else:
                if train > black_best:
                    black_best = train
            again = False
            train = 0

        # WHITE

        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if move_table[i][j] == self._WHITE:
                    train += 1
                elif move_table[i][j] == self._GREEN:
                    train += 0.5
                elif move_table[i][j] == self._BLACK:
                    if again:
                        if train < 4.5:
                            train = 0
                        else:
                            white_best = 5
                    else:
                        again = True
                        if train > white_best:
                            white_best = train
                        train = 0
                else:
                    if train > white_best:
                        white_best = train
                    train = 0
            if again:
                if train >= 4.5:
                    white_best = 5
            else:
                if train > white_best:
                    white_best = train
            again = False
            train = 0

        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if move_table[j][i] == self._WHITE:
                    train += 1
                elif move_table[j][i] == self._GREEN:
                    train += 0.5
                elif move_table[j][i] == self._BLACK:
                    if again:
                        if train < 4.5:
                            train = 0
                        else:
                            white_best = 5
                    else:
                        again = True
                        if train > white_best:
                            white_best = train
                        train = 0
                else:
                    if train > white_best:
                        white_best = train
                    train = 0
            if again:
                if train >= 4.5:
                    white_best = 5
            else:
                if train > white_best:
                    white_best = train
            again = False
            train = 0

        if white_best - 1 > black_best:
            return white_best * (-1)
        return black_best

    def minmax(self, move_table: [], depth: int, maximizing_player: bool):
        """Algorytm minmax."""
        if depth == 0:
            return self.evaluation(move_table)

        values = []
        if maximizing_player:
            values.append(-10000)
            for i in range(self._BOARD_SIZE):
                for j in range(self._BOARD_SIZE):
                    if move_table[i][j] == self._GREEN:
                        new_move_table = copy.deepcopy(move_table)
                        new_move_table[i][j] = self._BLACK
                        if i != 0:
                            if j != 0:
                                if new_move_table[i - 1][j - 1] == self._EMPTY:
                                    new_move_table[i - 1][j - 1] = self._GREEN
                            if new_move_table[i - 1][j] == self._EMPTY:
                                new_move_table[i - 1][j] = self._GREEN
                            if j != self._BOARD_SIZE - 1:
                                if new_move_table[i - 1][j + 1] == self._EMPTY:
                                    new_move_table[i - 1][j + 1] = self._GREEN
                        if j != 0:
                            if new_move_table[i][j - 1] == self._EMPTY:
                                new_move_table[i][j - 1] = self._GREEN
                        if j != self._BOARD_SIZE - 1:
                            if new_move_table[i][j + 1] == self._EMPTY:
                                new_move_table[i][j + 1] = self._GREEN
                        if i != self._BOARD_SIZE - 1:
                            if j != 0:
                                if new_move_table[i + 1][j - 1] == self._EMPTY:
                                    new_move_table[i + 1][j - 1] = self._GREEN
                            if new_move_table[i + 1][j] == self._EMPTY:
                                new_move_table[i + 1][j] = self._GREEN
                            if j != self._BOARD_SIZE - 1:
                                if new_move_table[i + 1][j + 1] == self._EMPTY:
                                    new_move_table[i + 1][j + 1] = self._GREEN
                        values.append(self.minmax(new_move_table, depth - 1, False))
            return max(values)
        else:
            values.append(10000)
            for i in range(self._BOARD_SIZE):
                for j in range(self._BOARD_SIZE):
                    if move_table[i][j] == self._GREEN:
                        new_move_table = copy.deepcopy(move_table)
                        new_move_table[i][j] = self._WHITE
                        if i != 0:
                            if j != 0:
                                if new_move_table[i - 1][j - 1] == self._EMPTY:
                                    new_move_table[i - 1][j - 1] = self._GREEN
                            if new_move_table[i - 1][j] == self._EMPTY:
                                new_move_table[i - 1][j] = self._GREEN
                            if j != self._BOARD_SIZE - 1:
                                if new_move_table[i - 1][j + 1] == self._EMPTY:
                                    new_move_table[i - 1][j + 1] = self._GREEN
                        if j != 0:
                            if new_move_table[i][j - 1] == self._EMPTY:
                                new_move_table[i][j - 1] = self._GREEN
                        if j != self._BOARD_SIZE - 1:
                            if new_move_table[i][j + 1] == self._EMPTY:
                                new_move_table[i][j + 1] = self._GREEN
                        if i != self._BOARD_SIZE - 1:
                            if j != 0:
                                if new_move_table[i + 1][j - 1] == self._EMPTY:
                                    new_move_table[i + 1][j - 1] = self._GREEN
                            if new_move_table[i + 1][j] == self._EMPTY:
                                new_move_table[i + 1][j] = self._GREEN
                            if j != self._BOARD_SIZE - 1:
                                if new_move_table[i + 1][j + 1] == self._EMPTY:
                                    new_move_table[i + 1][j + 1] = self._GREEN
                        values.append(self.minmax(new_move_table, depth - 1, True))
            return min(values)

    def ai_move(self):
        """Funkcja AI gry."""
        depth = 2
        move_table = self.ai_move_table()
        values = [[10000 for x in range(self._BOARD_SIZE)] for y in range(self._BOARD_SIZE)]

        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if move_table[i][j] == self._GREEN:
                    new_move_table = copy.deepcopy(move_table)
                    new_move_table[i][j] = self._current_player
                    if i != 0:
                        if j != 0:
                            if new_move_table[i - 1][j - 1] == self._EMPTY:
                                new_move_table[i - 1][j - 1] = self._GREEN
                        if new_move_table[i - 1][j] == self._EMPTY:
                            new_move_table[i - 1][j] = self._GREEN
                        if j != self._BOARD_SIZE - 1:
                            if new_move_table[i - 1][j + 1] == self._EMPTY:
                                new_move_table[i - 1][j + 1] = self._GREEN
                    if j != 0:
                        if new_move_table[i][j - 1] == self._EMPTY:
                            new_move_table[i][j - 1] = self._GREEN
                    if j != self._BOARD_SIZE - 1:
                        if new_move_table[i][j + 1] == self._EMPTY:
                            new_move_table[i][j + 1] = self._GREEN
                    if i != self._BOARD_SIZE - 1:
                        if j != 0:
                            if new_move_table[i + 1][j - 1] == self._EMPTY:
                                new_move_table[i + 1][j - 1] = self._GREEN
                        if new_move_table[i + 1][j] == self._EMPTY:
                            new_move_table[i + 1][j] = self._GREEN
                        if j != self._BOARD_SIZE - 1:
                            if new_move_table[i + 1][j + 1] == self._EMPTY:
                                new_move_table[i + 1][j + 1] = self._GREEN
                    values[i][j] = self.minmax(new_move_table, depth, True)

        # for line in values:
        #     print(line)
        #
        # print("\n\n")

        min_values = []
        for line in values:
            min_values.append(min(line))
        min_value = min(min_values)

        if self._current_player == self._BLACK:
            self.player_swap()

        for i in range(self._BOARD_SIZE):
            for j in range(self._BOARD_SIZE):
                if values[i][j] == min_value:
                    self._BOARD[i][j] = self._current_player
                    return

    def check_method_1(self):
        """Funkcja sprawdza w poziomie."""
        train = 0
        draw = 1
        for i in range(0, self._BOARD_SIZE):
            for j in range(0, self._BOARD_SIZE):
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
        return self.GOING_ON

    def check_method_2(self):
        """Funkcja sprawdza w pionie."""
        train = 0
        for i in range(0, self._BOARD_SIZE):
            for j in range(0, self._BOARD_SIZE):
                if self._BOARD[j][i] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def check_method_3(self):
        """Funkcja sprawdza na skos."""
        train = 0
        for i in range(0, self._BOARD_SIZE):
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
        """Funkcja sprawdza na skos."""
        train = 0
        for j in range(1, self._BOARD_SIZE):
            for i in range(0, self._BOARD_SIZE - j):
                if self._BOARD[self._BOARD_SIZE - 1 - i][j + i] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def check_method_5(self):
        """Funkcja sprawdza na skos."""
        train = 0
        for i in range(0, self._BOARD_SIZE):
            for j in range(0, i + 1):
                if self._BOARD[i - j][self._BOARD_SIZE - 1 - j] == self._current_player:
                    train += 1
                    if train == 5:
                        return self.VICTORY
                else:
                    train = 0
            train = 0
        return self.GOING_ON

    def check_method_6(self):
        """Funkcja sprawdza na skos."""
        train = 0
        for j in range(0, self._BOARD_SIZE - 1):
            for i in range(0, j + 1):
                if self._BOARD[self._BOARD_SIZE - 1 - i][j - i] == self._current_player:
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
        """Zamiana aktualnego gracza."""
        if self._current_player == self._BLACK:
            self._current_player = self._WHITE
        else:
            self._current_player = self._BLACK

    def new_game(self):
        """Powrót do startowego stanu gry."""
        self._current_player = self._BLACK
        self._output_info = self._PLAY
        self._status = self._PLAY
        self._BOARD = [[self._EMPTY for x in range(self._BOARD_SIZE)]
                       for y in range(self._BOARD_SIZE)]

    def get_board_size(self):
        """Zwraca rozmiar planszy."""
        return self._BOARD_SIZE

    def get_board(self):
        """Zwraca planszę."""
        return self._BOARD

    def get_status(self):
        """Zwraca status gry."""
        return self._status

    def get_current_player(self):
        """Zwraca aktualnego gracza."""
        return self._current_player

    def get_output_info(self):
        """Zwraca informację z logiki gry."""
        return self._output_info

    def play(self, wspolrzedne: str):
        """Główna funkcja gry."""
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
        except (ex.BadCoordinatesException,
                ex.FieldOccupiedException,
                ex.GameOverException,
                ex.UndefinedException) as err:
            self._output_info = f'{err.print_message()} {self.get_status()}'
        else:
            self._output_info = self.get_status()
