import random
from typing import List, Optional

from board.board import IBoard
from position.position import Position
from stone.stone import Stone


class Player:
    """
    プレイヤーのクラス
    置けるところからランダムで置く

    Attributes:
    -----------
    stone : Stone
    """
    def __init__(self, stone: Stone):
        self.stone: Stone = stone

    def select(self, board: IBoard) -> Optional[Position]:
        """
        置けるところをランダムに選ぶ

        Parameters:
        -----------
        board : Board
            ボード

        Returns:
        --------
        Position
            置ける場所があるとき, ランダムに選んで返す
        None
            置ける場所がないとき
        """
        available_positions: List[Position] = \
            board.get_available_positions(self.stone)

        if available_positions:
            return random.choice(available_positions)
        else:
            return None
