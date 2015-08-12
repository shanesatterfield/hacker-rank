from __future__ import print_function, division
import sys, re, time

move_list  = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'CLEAN']
block_dict = {'bot': 'b', 'tile': '-', 'target': 'd'}

def next_move( r, c, grid ):
    global move_list
    global block_dict
    move = None

    # Find all dirty rooms. If none are found, you are done.
    dirty_rooms = find_ds(grid, block_dict['target'])
    if not dirty_rooms:
        return move

    # Sort the dirty rooms into a predicatble order.
    dirty_rooms = sorted(dirty_rooms, key=lambda x: abs(x[0] - r) + abs(x[1] - c) )

    dr = dirty_rooms[0]

    # Clean a room if you are in a dirty room.
    if grid[r][c] == block_dict['target']:
        move = move_list[-1]

    # Move up or down depending on the row difference.
    elif r != dr[0]:
        move = move_list[int(dr[0] > r)]

    # Move left or right depending on the row difference.
    elif c != dr[1]:
        move = move_list[int(dr[1] > c)+2]

    return move


def mod_grid( r, c, grid, movement ):
    """Take an old grid and return a new grid that is modified by the command"""
    global move_list
    global block_dict
    nr, nc = r, c

    # If you are cleaning, you don't need to move.
    if movement == move_list[-1]:
        grid = swap_val( r, c, grid, block_dict['bot'] )

    else:
        # If you were just on a tile, not a bomb, and are moving, clear it.
        if grid[r][c] == block_dict['bot']:
            grid = swap_val( r, c, grid, block_dict['tile'] )

        # Move according to the movement specified.
        if movement == move_list[0]:
            nr -= 1
        elif movement == move_list[1]:
            nr += 1
        elif movement == move_list[2]:
            nc -= 1
        elif movement == move_list[3]:
            nc += 1

        # If you did not move onto a dirty room, draw yourself to replace tile.
        if grid[nr][nc] != block_dict['target']:
            grid = swap_val( nr, nc, grid, block_dict['bot'] )

    return nr, nc, grid

def swap_val( r, c, grid, char ):
    """Swaps a char in a grid."""
    grid[r] = grid[r][:c] + char + grid[r][c+1:]
    return grid


def find_ds( grid, string ):
    """Finds all instances of string in the grid and returns indices."""
    rows, columns = len(grid), len(grid[0])
    return [ (x.start()//rows, x.start()%columns) for x in re.finditer(string, ''.join(grid)) ]

def main():
    lines = sys.stdin.readlines()
    r, c = [ int(x) for x in lines[0].split() ]
    grid = [ x.strip() for x in lines[1:] ]

    print(next_move(r, c, grid))

if __name__ == '__main__':
    main()
