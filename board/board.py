from stone.stone import Stone
from position.position import Position


class IBoard:
    def put_stone(self, stone: Stone, position: Position):
        raise NotImplementedError()

    def finished(self):
        raise NotImplementedError()


class Board(IBoard):
    """
    Attributes:
    -----------
    data : List[List[Stone or None]]
    """

    SIZE = 4

    def __init__(self):
        self.data: List[List[Stone or None]] \
                = [[None] * self.SIZE for i in range(self.SIZE)]

    def put_stone(self, stone: Stone, position: Position):
        assert self.data[position.x][position.y] is None
        self.data[position.x][position.y] = stone

    def finished(self) -> bool:
        return True
