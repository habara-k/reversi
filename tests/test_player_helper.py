import unittest

from stone.stone import Stone
from position.position import Position
from board.board import Board
from playerhelper.player_helper import PlayerHelper


class TestPlayerHelper(unittest.TestCase):
    def setUp(self):
        self.player_helper: PlayerHelper = PlayerHelper()
        self.board: Board = Board()

    def test_select(self):
        self.assertIsInstance(self.player_helper.select(self.board), Position)

    def test_stone(self):
        self.assertIsInstance(self.player_helper.stone(), Stone)

    def test_swap(self):
        self.assertEqual(self.player_helper.player.stone, Stone.BLACK)
        self.player_helper.swap()
        self.assertEqual(self.player_helper.player.stone, Stone.WHITE)


if __name__ == "__main__":
    unittest.main()
