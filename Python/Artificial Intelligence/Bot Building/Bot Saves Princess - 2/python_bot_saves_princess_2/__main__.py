from __future__ import print_function, division
import sys, time
from grid import Grid

def save_princess_2( r, c, grid ):
    p_loc = find_princess(grid, 'p')
    temp_r, temp_c = r, c
    maze = Grid( grid )
    maze.start()

    movement_list = list()

    while r != p_loc[0] or c != p_loc[1]:
        movement = next_move(r, c, p_loc[0], p_loc[1])

        if movement is 'UP':
            temp_r -= 1
        elif movement is 'DOWN':
            temp_r += 1
        elif movement is 'LEFT':
            temp_c -= 1
        elif movement is 'RIGHT':
            temp_c += 1

        grid[r]      = grid[r][:c] + '-' + grid[r][c+1:]
        grid[temp_r] = grid[temp_r][:temp_c] + 'm' + grid[temp_r][temp_c+1:]
        r, c         = temp_r, temp_c

        maze.set_grid_data( grid )

        movement_list.append( movement )
        time.sleep(0.1)

    return movement_list

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
