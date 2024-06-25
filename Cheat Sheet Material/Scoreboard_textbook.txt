class Scoreboard:
    """Fixed-length sequence of high scores in nondecreasing order."""

    def __init__(self, capacity=10):
        """Initialize scoreboard with given maximum capacity.

        All entries are initially None.
        """
        self.board = [None] * capacity  # reserve space for future scores
        self.n = 0  # number of actual entries

    def __getitem__(self, k):
        """Return entry at index k."""
        return self.board[k]

    def __str__(self):
        """Return string representation of the high score list."""
        return "\n".join(str(self.board[j]) for j in range(self.n))

    def add(self, entry):
        """Consider adding entry to high scores."""
        score = entry.get_score()

        # Does new entry qualify as a high score?
        # answer is yes if board not full or score is higher than last entry
        good = self.n < len(self.board) or score > self.board[-1].get_score()

        if good:
            if self.n < len(self.board):  # no score drops from list
                self.n += 1  # so overall number increases

            # shift lower scores rightward to make room for new entry
            j = self.n - 1
            while j > 0 and self.board[j - 1].get_score() < score:
                self.board[j] = self.board[j - 1]  # shift entry from j-1 to j
                j -= 1  # and decrement j
            self.board[j] = entry  # when done, add new entry


# Example of an Entry class to work with Scoreboard
class Entry:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_score(self):
        return self.score

    def __str__(self):
        return f"{self.name}: {self.score}"


# Example usage
if __name__ == "__main__":
    scoreboard = Scoreboard(5)
    scoreboard.add(Entry("Alice", 50))
    scoreboard.add(Entry("Bob", 70))
    scoreboard.add(Entry("Charlie", 60))
    print(scoreboard)
