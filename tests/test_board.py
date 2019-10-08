import unittest

from stone.stone import Stone
from position.position import Position
from board.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self):
        self.board: Board = Board()

    def test_init(self):
        SIZE = self.board.SIZE
        tests = [
                [SIZE//2-1, SIZE//2-1, Stone.WHITE],
                [SIZE//2,   SIZE//2,   Stone.WHITE],
                [SIZE//2-1, SIZE//2,   Stone.BLACK],
                [SIZE//2,   SIZE//2-1, Stone.BLACK],
                ]
        for x, y, stone in tests:
            self.assertEqual(self.board.data[x][y], stone)

    def test_put_stone(self):
        SIZE = self.board.SIZE
        puts = [
                [SIZE//2-1, SIZE//2-2, Stone.BLACK],
                ]

        tests = [
                [SIZE//2-1, SIZE//2-2, Stone.BLACK],
                [SIZE//2-1, SIZE//2-1, Stone.BLACK],
                ]
        for x, y, stone in puts:
            self.board.put_stone(stone, Position(x, y))

        for x, y, stone in tests:
            self.assertEqual(self.board.data[x][y], stone)

    def test_get_stone(self):
        SIZE = self.board.SIZE
        tests = [
                [SIZE//2-1, SIZE//2-1, Stone.WHITE],
                [SIZE//2,   SIZE//2,   Stone.WHITE],
                [SIZE//2-1, SIZE//2,   Stone.BLACK],
                [SIZE//2,   SIZE//2-1, Stone.BLACK],
                ]
        for x, y, stone in tests:
            self.assertEqual(self.board.get_stone(Position(x, y)), stone)


if __name__ == "__main__":
    unittest.main()
