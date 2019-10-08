import random
from typing import List, Optional

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

    def select(self, board: IBoard) -> Optional[Position]:
        available_positions: List[Position] = \
                board.get_available_positions(self.stone)

        if available_positions:
            return random.choice(available_positions)
        else:
            return None
