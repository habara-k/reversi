from enum import Enum


class Stone(Enum):
    """
    石の列挙型
    """
    BLACK = 1
    WHITE = 2

    def opponent(self):
        """
        相手の石を返す

        Returns:
        --------
        Stone
            相手の石
        """

        return self.BLACK if self == self.WHITE else self.WHITE
