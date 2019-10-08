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
            position: Position = self.player_helper.select(self.board)
            self.board.put_stone(self.player_helper, position)
            if self.board.finished():
                break
            self.player_helper.swap()
