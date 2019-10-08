from typing import List

from stone.stone import Stone
from position.position import Position


class IBoard:
    def put_stone(self, stone: Stone, position: Position):
        raise NotImplementedError()

    def finished(self):
        raise NotImplementedError()

    def get_stone(self, position: Position) -> Stone:
        raise NotImplementedError()

    def get_available_positions(self, stone: Stone) -> List[Position]:
        raise NotImplementedError()



class Board(IBoard):
    """
    Attributes:
    -----------
    data : List[List[Stone]]
    time : int
    """

    SIZE = 4
    TIME_MAX = SIZE**2

    def __init__(self):
        self.time: int = 0
        self.data: List[List[Stone]] = \
            [[Stone.NONE] * self.SIZE for i in range(self.SIZE)]

        first_stones = [
                [self.SIZE//2-1, self.SIZE//2-1, Stone.WHITE],
                [self.SIZE//2,   self.SIZE//2,   Stone.WHITE],
                [self.SIZE//2-1, self.SIZE//2,   Stone.BLACK],
                [self.SIZE//2,   self.SIZE//2-1, Stone.BLACK],
                ]
        for x, y, stone in first_stones:
            self.data[x][y] = stone

    def put_stone(self, stone: Stone, position: Position):
        assert self.get_stone(position) == Stone.NONE
        assert self.time < self.TIME_MAX

        reversible_positions = self._reversible_positions(stone, position)
        assert reversible_positions

        self.data[position.x][position.y] = stone
        for pos in reversible_positions:
            self.data[pos.x][pos.y] = stone

        self.time += 1

    def finished(self) -> bool:
        return self.time == self.TIME_MAX

    def get_stone(self, position: Position) -> Stone:
        return self.data[position.x][position.y]

    def get_available_positions(self, stone: Stone) -> List[Position]:
        """
        stone が置けるposition のListを返す
        """
        available_positions: List[Position] = []
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                position: Position = Position(x, y)
                if self._reversible_positions(stone, position):
                    available_positions.append(position)

        return available_positions

    def _reversible_positions(self, stone: Stone, position: Position) \
            -> List[Position]:
        """
        stone をposition に置いたときに挟める相手の石を返す
        """
        if self.get_stone(position) != Stone.NONE:
            return []

        reversible_positions: List[Position] = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                reversible_positions.extend(
                        self._reversible_positions_on_direction(
                            stone, position, dx, dy))

        return reversible_positions

    def _reversible_positions_on_direction(
            self, stone: Stone, position: Position,
            dx: int, dy: int) -> List[Position]:
        """
        stone をposition に置いたとき,
        (dx, dy) の方向で挟める相手の石を返す
        """
        x: int = position.x + dx
        y: int = position.y + dy

        reversible_positions: List[Position] = []
        finish_stone: Stone = Stone.NONE

        while 0 <= x < self.SIZE and 0 <= y < self.SIZE:
            if self.data[x][y] != stone.opponent():
                finish_stone = self.data[x][y]
                break
            reversible_positions.append(Position(x, y))
            x += dx
            y += dy

        if finish_stone != stone:
            reversible_positions = []

        return reversible_positions
