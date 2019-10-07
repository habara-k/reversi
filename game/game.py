from playerhelper.playerhelper import PlayerHelper
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
            self._play()
            if self._finished():
                break
            self._swap()

    def _play(self):
        position: Position = self.player_helper.select(self.board)
        self.board.put_stone(self.player_helper, position)

    def _finished(self) -> bool:
        return self.board.finished()

    def _swap(self):
        self.player_helper.swap()
