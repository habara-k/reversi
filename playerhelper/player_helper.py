from typing import List, Optional

from board.board import IBoard
from position.position import Position
from player.player import Player
from stone.stone import Stone


class PlayerHelper:
    """
    プレイヤーのヘルパークラス

    Attributes:
    -----------
    players : List[Player]
        2人のプレイヤー
    player : Player
        手番のプレイヤー
    """
    def __init__(self):
        self.players: List[Player] = [Player(Stone.BLACK), Player(Stone.WHITE)]
        self.player: Player = self.players[0]

    def select(self, board: IBoard) -> Optional[Position]:
        """
        置く場所を返す

        Parameters:
        -----------
        board : IBoard
            ボードのインターフェース

        Returns:
        --------
        Position
            置ける場所があるとき
        None
            置ける場所がないとき
        """
        return self.player.select(board)

    def stone(self) -> Stone:
        """
        手番のプレイヤーの石を返す

        Returns:
        --------
        Stone
            手番のプレイヤーの石
        """
        return self.player.stone

    def swap(self):
        """
        手番のプレイヤーを入れ替える
        """
        if self.player == self.players[0]:
            self.player = self.players[1]
        else:
            self.player = self.players[0]
