from typing import Optional

from playerhelper.player_helper import PlayerHelper
from board.board import Board
from position.position import Position


class Game:
    """
    Attributes:
    -----------
    player_helper: PlayerHelper
    board: Board
    """
    def __init__(self):
        self.player_helper: PlayerHelper = PlayerHelper()
        self.board: Board = Board()

    def start(self):
        while True:
            position: Optional[Position] = self.player_helper.select(self.board)
            if position is not None:
                self.board.put_stone(self.player_helper.stone(), position)
            else:
                self.board.pass_turn()
            if self.board.finished():
                break
            self.player_helper.swap()

        winner_stone: Optional[Stone] = self.board.get_winner_stone()

        print("winner_stone:", winner_stone)
