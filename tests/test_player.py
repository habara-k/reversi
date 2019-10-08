import unittest

from stone.stone import Stone
from position.position import Position
from board.board import Board
from player.player import Player


class TestPlayer(unittest.TestCase):
    def setUp(self):
        self.stone: Stone = Stone.BLACK
        self.player: Player = Player(self.stone)
        self.board: Board = Board()

    def test_init(self):
        self.assertEqual(self.player.stone, self.stone)

    def test_select(self):
        self.assertIsInstance(self.player.select(self.board), Position)


if __name__ == "__main__":
    unittest.main()
