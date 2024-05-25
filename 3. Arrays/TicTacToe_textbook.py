class TicTacToe:
    """Management of a Tic-Tac-Toe game (does not do strategy)."""

    def __init__(self):
        """Start a new game."""
        self.board = [[" "] * 3 for j in range(3)]  # Create a 3x3 game board
        self.player = "X"  # Player X starts the game

    def mark(self, i, j):
        """Put an X or O mark at position (i,j) for next player's turn."""
        if not (0 <= i <= 2 and 0 <= j <= 2):
            raise ValueError("Invalid board position")
        if self.board[i][j] != " ":
            raise ValueError("Board position occupied")
        if self.winner() is not None:
            raise ValueError("Game is already complete")
        self.board[i][j] = self.player  # Mark the position with current player's mark
        if self.player == "X":
            self.player = "O"  # Switch to player O for next turn
        else:
            self.player = "X"  # Switch to player X for next turn

    def is_win(self, mark):
        """Check whether the board configuration is a win for the given player."""
        board = self.board  # local variable for shorthand
        return (
            mark == board[0][0] == board[0][1] == board[0][2]  # row 0
            or mark == board[1][0] == board[1][1] == board[1][2]  # row 1
            or mark == board[2][0] == board[2][1] == board[2][2]  # row 2
            or mark == board[0][0] == board[1][0] == board[2][0]  # column 0
            or mark == board[0][1] == board[1][1] == board[2][1]  # column 1
            or mark == board[0][2] == board[1][2] == board[2][2]  # column 2
            or mark == board[0][0] == board[1][1] == board[2][2]  # diagonal
            or mark == board[0][2] == board[1][1] == board[2][0]
        )  # rev diagonal

    def winner(self):
        """Return mark of winning player, or None to indicate a tie."""
        for mark in ["X", "O"]:
            if self.is_win(mark):
                return mark  # Return the winning player's mark
        return None  # Return None if there is no winner (tie)

    def __str__(self):
        """Return string representation of current game board."""
        rows = [
            " | ".join(self.board[r]) for r in range(3)
        ]  # Create rows of the game board
        return "\n-----\n".join(rows)  # Join rows with separator and return as a string
