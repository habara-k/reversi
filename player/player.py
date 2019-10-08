from board.board import IBoard
from position.position import Position
from stone.stone import Stone


class Player:
    """
    Attributes:
    -----------
    stone : Stone
    """
    def __init__(self, stone: Stone):
        self.stone: Stone = stone

    def select(self, board: IBoard) -> Position:
        return Position(0, 0)
