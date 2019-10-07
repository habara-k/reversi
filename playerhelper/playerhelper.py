from board.board import BoardImpl
from position.position import Position


class PlayerHelperImpl:
    def select(self, board: BoardImpl) -> Position:
        raise NotImplementedError()

    def swap(self):
        raise NotImplementedError()


class PlayerHelper(PlayerHelperImpl):
    def select(self, board: BoardImpl) -> Position:
        return Position()

    def swap(self):
        pass
