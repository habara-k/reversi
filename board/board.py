from stone.stone import Stone
from position.position import Position


class BoardImpl:
    def put_stone(self, stone: Stone, position: Position):
        raise NotImplementedError()

    def finished(self):
        raise NotImplementedError()


class Board(BoardImpl):
    def put_stone(self, stone: Stone, position: Position):
        pass

    def finished(self) -> bool:
        return True
