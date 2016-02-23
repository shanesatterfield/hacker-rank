from __future__ import print_function, division
import sys

class pe_006:
    def __init__(self, starting_squares=1000):
        """Initialize the object with the number of squares that you want precalculated."""
        self.squares = []
        self.diffs   = dict()
        self.find_squares(starting_squares)

    def find_diff(self, N):
        """Find the difference of the square of sums and the sum of squares from 1 to N."""
        # If the answer has been cached, then return it.
        if N in self.diffs:
            return self.diffs[N]

        # If not cached, calculate the difference. Make use of cached squares.
        self.find_squares(N)

        # Find the result, cache it and return it.
        self.diffs[N] = pe_006.get_square_of_sums(N) - sum(self.get_squares(1, N))
        return self.diffs[N]

    def get_squares(self, start, stop):
        """Safely retrieve a range of squares."""
        start = max(start, 1)
        if stop >= len(self.squares):
            self.find_squares(stop)
        return self.squares[start:stop+1]

    @staticmethod
    def get_square_of_sums(N):
        """Finds the square of consecutive sums."""
        return int((N+1) * N/2)**2

    def find_squares(self, new_max):
        """If the new max square is beyond the currently cached ones, cache up to that point."""
        self.squares.extend([pow(n,2) for n in range(len(self.squares), new_max+1)])

def main():
    T = int(input())
    lines = [int(x.strip()) for x in sys.stdin.readlines()[:T]]
    differ = pe_006()
    for line in lines:
        print(differ.find_diff(line))

if __name__ == '__main__':
    main()
