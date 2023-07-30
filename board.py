from unit import Unit
class Board:

    def __init__(self, rows=10, cols=10):
        self.board = [[Unit() for i in range(cols)] for j in range(rows)]

    @property
    def board(self):
        return self._board
    @board.setter
    def board(self, r, c, value):
        self._board[r][c] = value

    def get_unit(self, r, c):
        return self.board[r][c]
