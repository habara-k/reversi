import unittest

from stone.stone import Stone


class TestStone(unittest.TestCase):
    def test_opponent(self):
        stone: Stone = Stone.BLACK
        self.assertEqual(stone.opponent(), Stone.WHITE)


if __name__ == "__main__":
    unittest.main()
