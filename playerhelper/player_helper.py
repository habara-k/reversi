from typing import List

from board.board import IBoard
from position.position import Position
from player.player import Player
from stone.stone import Stone


class PlayerHelper:
    """
    Attributes:
    -----------
    players : List[Player]
    player : Player
    """
    def __init__(self):
        self.players: List[Player] = [Player(Stone.BLACK), Player(Stone.WHITE)]
        self.player: Player = self.players[0]

    def select(self, board: IBoard) -> Position:
        return Position(0, 0)

    def stone(self) -> Stone:
        return self.player.stone

    def swap(self):
        if self.player == self.players[0]:
            self.player = self.players[1]
        else:
            self.player = self.players[0]
