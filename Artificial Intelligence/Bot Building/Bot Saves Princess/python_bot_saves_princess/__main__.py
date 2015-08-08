from __future__ import print_function, division
import sys
from itertools import repeat

def save_princess( grid ):
    """Returns a list of moves the player must take to save the princess."""
    if type(grid) is str: grid = grid.split('\n')

    N            = len(grid[0])
    princess_loc = find_princess( grid, 'p' )
    bot_loc      = (N//2, N//2)

    return get_moves( princess_loc, bot_loc )

def get_moves( princess_loc, bot_loc ):
    """Returns a list of string moves to get to the princess."""
    loc = (
        int(princess_loc[0] > bot_loc[0]),
        int(princess_loc[1] > bot_loc[1])+2,
    )

    moves_list = ['UP', 'DOWN', 'LEFT', 'RIGHT']

    moves = list(repeat(moves_list[loc[0]], bot_loc[0]))
    moves.extend(repeat(moves_list[loc[1]], bot_loc[0]))

    return moves

def find_princess( grid, princess_char ):
    """Returns a tuple of the location of the princess. (Row, Column)"""
    N = len(grid[0])
    loc = ''.join(grid).index( princess_char )
    return (loc//N, loc%N)

def main():
    """Takes stdin, parses it and runs it through functions to output."""
    T = int(input())
    grid = sys.stdin.readlines()[:T]
    grid = [ x[:T] for x in grid ]

    for n in save_princess( grid ):
        print( n )

if __name__ == '__main__':
    main()
