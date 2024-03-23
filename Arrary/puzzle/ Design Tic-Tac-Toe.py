class TicTacToe:
    def __init__(self, n):
        self.rows = [0] * n
        self.cols = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row, col, player):
        move = 1 if player == 1 else -1
        size = len(self.rows)

        self.rows[row] += move
        self.cols[col] += move

        if row == col:
            self.diagonal += move

        if col == (size - row - 1):
            self.anti_diagonal += move

        if (
            abs(self.rows[row]) == size
            or abs(self.cols[col]) == size
            or abs(self.diagonal) == size
            or abs(self.anti_diagonal) == size
        ):
            return player

        return 0


# Example of usage:
# obj = TicTacToe(n)  # Initialize with board size 'n'
# param_1 = obj.move(row, col, player)  # Make a move for the given player at (row, col)

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
