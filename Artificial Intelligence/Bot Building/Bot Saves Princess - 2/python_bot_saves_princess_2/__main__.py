from __future__ import print_function, division
import sys

def save_princess_2( r, c, grid ):
    p_loc = find_princess(grid, 'p')
    return next_move(r, c, p_loc[0], p_loc[1])

def find_princess( grid, princess_char ):
    N = len(grid[0])
    p_loc = ''.join( grid ).index( princess_char )
    return p_loc // N, p_loc % N

def next_move( br, bc, pr, pc ):
    move = None
    if br != pr:
        move = next_move.move_list[int(pr > br)]
    elif bc != pc:
        move = next_move.move_list[int(pc > bc)+2]
    return move

next_move.move_list = ['UP', 'DOWN', 'LEFT', 'RIGHT']

def main():
    T = int(input())
    lines = [ x.strip() for x in sys.stdin.readlines()[:T+1] ]
    r, c = [ int(x) for x in lines[0].split() ]
    lines = lines[1:]

    print(save_princess_2(r, c, lines))

if __name__ == '__main__':
    main()
