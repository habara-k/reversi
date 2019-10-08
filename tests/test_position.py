import unittest

from position.position import Position


class TestPosition(unittest.TestCase):
    def test_init(self):
        tests = [
                [0, 0],
                [1, 3],
                ]
        for x, y in tests:
            position: Position = Position(x, y)
            self.assertEqual(position.x, x)
            self.assertEqual(position.y, y)


if __name__ == "__main__":
    unittest.main()
