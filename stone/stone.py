from enum import Enum


class Stone(Enum):
    BLACK = 1
    WHITE = 2
    NONE = 3

    def opponent(self):
        assert self != self.NONE
        if self == self.BLACK:
            return self.WHITE
        else:
            return self.BLACK
