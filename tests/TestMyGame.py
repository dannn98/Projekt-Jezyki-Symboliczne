import unittest
# from unittest.mock import Mock
from myexception import FieldOccupiedException, BadCoordinatesException
from mygame import MyGame


class TestMyGame(unittest.TestCase):
    def setUp(self):
        self.game = MyGame()

    def test_player_move(self):
        self.game.player_move("a1")
        self.assertEqual(self.game._BOARD[0][0], 'X')
        self.assertNotEqual(self.game._BOARD[0][0], 'O')
        self.assertNotEqual(self.game._BOARD[0][0], '.')

        with self.assertRaises(FieldOccupiedException):
            self.game.player_move("a1")

        with self.assertRaises(BadCoordinatesException):
            self.game.player_move("a111")

    def test_new_game(self):
        self.game.player_move("a1")
        self.game.new_game()
        for i in range(15):
            self.assertEqual(self.game._BOARD[i][:], ['.' for j in range(15)])

        self.assertEqual(self.game._current_player, 'X')
        self.assertEqual(self.game._status, "Podaj współrzędne (np. b13)")
        self.assertEqual(self.game._output_info, "Podaj współrzędne (np. b13)")

    def test_player_swap(self):
        self.game.player_swap()
        self.assertEqual(self.game._current_player, 'O')
        self.game.player_swap()
        self.assertEqual(self.game._current_player, 'X')

    def test_status_check(self):
        self.game.player_move("a1")
        self.game.player_move("a2")
        self.game.player_move("a3")
        self.game.player_move("a4")
        self.game.player_move("a5")
        self.game.status_check()

        self.assertEqual(self.game._status, "CZARNE WYGRAŁY!")
