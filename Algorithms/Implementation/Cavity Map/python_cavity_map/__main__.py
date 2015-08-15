from __future__ import print_function, division
import sys

def is_cavity( row, column, grid ):
    """Check if space is not a wall and is greater than all adjacent squares."""
    return not is_wall( row, column, len(grid) ) and all(map(lambda x: grid[row][column] > grid[x[0]][x[1]], gen_adjacents(row, column)))

def gen_adjacents( row, column):
    """Generates a list of row, column pairs that correspond to adjancent spaces"""
    return [(row-1, column), (row+1, column), (row, column-1), (row, column+1)]

def is_wall( row, column, N ):
    """Returns True if value is a wall space."""
    return row == 0 or row == N-1 or column == 0 or column == N-1

def main():
    N = int(input())
    grid = [ x.strip() for x in sys.stdin.readlines()[:N] ]

    # Evaluate each value in grid to check if it is a cavity.
    for row in range(len(grid)):
        for column in range(len(grid[row])):
            if is_cavity( row, column, grid ):
                print('X', end='')
            else:
                print(grid[row][column], end='')
        print()


if __name__ == '__main__':
    main()
