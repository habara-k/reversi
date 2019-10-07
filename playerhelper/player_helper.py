from board.board import IBoard
from position.position import Position


class IPlayerHelper:
    def select(self, board: IBoard) -> Position:
        raise NotImplementedError()

    def swap(self):
        raise NotImplementedError()


class PlayerHelper(IPlayerHelper):
    def select(self, board: IBoard) -> Position:
        return Position()

    def swap(self):
        pass
