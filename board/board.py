from typing import List, Optional

from stone.stone import Stone
from position.position import Position


class IBoard:
    """
    ボードのインターフェース
    """
    def put_stone(self, stone: Stone, position: Position):
        raise NotImplementedError()

    def finished(self):
        raise NotImplementedError()

    def get_stone(self, position: Position) -> Optional[Stone]:
        raise NotImplementedError()

    def get_available_positions(self, stone: Stone) -> List[Position]:
        raise NotImplementedError()



class Board(IBoard):
    """
    ボードの実装クラス

    Attributes:
    -----------
    data : List[List[Optional[Stone]]]
        盤面を保持する2次元配列
    time : int
        経過したターン
    SIZE : int
        盤面の大きさ
    TIME_MAX : int
        最大経過ターン
    """

    SIZE = 4
    TIME_MAX = SIZE**2 - 4

    def __init__(self):
        self.time: int = 0
        self.data: List[List[Optional[Stone]]] = \
            [[None] * self.SIZE for i in range(self.SIZE)]

        first_stones = [
                [self.SIZE//2-1, self.SIZE//2-1, Stone.WHITE],
                [self.SIZE//2,   self.SIZE//2,   Stone.WHITE],
                [self.SIZE//2-1, self.SIZE//2,   Stone.BLACK],
                [self.SIZE//2,   self.SIZE//2-1, Stone.BLACK],
                ]
        for x, y, stone in first_stones:
            self.data[x][y] = stone

    def show(self):
        """
        盤面を表示する
        """
        print("time:", self.time)
        mark = {None: ".", Stone.BLACK: "x", Stone.WHITE: "o"}
        for row in self.data:
            print("".join([mark[s] for s in row]))
        print()

    def pass_turn(self):
        """
        手番をパスする
        置ける場所がないときに呼ぶ
        """
        self.time += 1

        self.show()

    def put_stone(self, stone: Stone, position: Position):
        """
        石を置く
        position に石が置けない場合はエラーを吐く

        Parameters:
        -----------
        stone : Stone
            置く石
        position : Position
            置く場所
        """
        assert position is not None
        assert self.get_stone(position) is None
        assert self.time < self.TIME_MAX

        reversible_positions = self._reversible_positions(stone, position)
        assert reversible_positions

        self.data[position.x][position.y] = stone
        for pos in reversible_positions:
            self.data[pos.x][pos.y] = stone

        self.time += 1

        self.show()

    def finished(self) -> bool:
        """
        ゲームの終了を判定する

        Returns:
        --------
        bool
            経過したターンが最大経過ターンかどうか

        """
        return self.time == self.TIME_MAX

    def get_winner_stone(self) -> Optional[Stone]:
        """
        勝者の石を返す
        引き分けの場合はNoneを返す
        """
        flat = [stone for row in self.data for stone in row]
        if flat.count(Stone.BLACK) > flat.count(Stone.WHITE):
            return Stone.BLACK
        elif flat.count(Stone.WHITE) > flat.count(Stone.BLACK):
            return Stone.WHITE
        else:
            return None

    def get_stone(self, position: Position) -> Optional[Stone]:
        return self.data[position.x][position.y]

    def get_available_positions(self, stone: Stone) -> List[Position]:
        """
        stone が置けるposition のListを返す

        Parameters:
        -----------
        stone : Stone
            置く石

        Returns:
        --------
        available_positions : List[Position]
            stone が置けるposition のList
        """
        available_positions: List[Position] = []
        for x in range(self.SIZE):
            for y in range(self.SIZE):
                position: Position = Position(x, y)
                if self._reversible_positions(stone, position):
                    available_positions.append(position)

        return available_positions

    def _reversible_positions(self, stone: Stone, position: Position) \
            -> List[Position]:
        """
        stone をposition に置いたときに挟める相手の石を返す

        Parameters:
        -----------
        stone : Stone
            置く石
        position : Position
            置く場所

        Returns:
        --------
        reversible_positions : List[Position]
            stone をposition に置いたときに挟める
            相手の石があるPosition のList
        """
        if self.get_stone(position) is not None:
            return []

        reversible_positions: List[Position] = []

        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                reversible_positions.extend(
                        self._reversible_positions_on_direction(
                            stone, position, dx, dy))

        return reversible_positions

    def _reversible_positions_on_direction(
            self, stone: Stone, position: Position,
            dx: int, dy: int) -> List[Position]:
        """
        stone をposition に置いたとき,
        (dx, dy) の方向で挟める相手の石を返す

        Parameters:
        -----------
        stone : Stone
            置く石
        position : Position
            置く場所
        dx : int
        dy : int
            挟む方向

        Returns:
        --------
        reversible_positions : List[Position]
            stone をposition に置いたとき
            (dx, dy) の方向で挟める相手の石があるPosition のList
        """
        x: int = position.x + dx
        y: int = position.y + dy

        reversible_positions: List[Position] = []
        finish_stone: Optional[Stone] = None

        while 0 <= x < self.SIZE and 0 <= y < self.SIZE:
            if self.data[x][y] != stone.opponent():
                finish_stone = self.data[x][y]
                break
            reversible_positions.append(Position(x, y))
            x += dx
            y += dy

        if finish_stone != stone:
            reversible_positions = []

        return reversible_positions
