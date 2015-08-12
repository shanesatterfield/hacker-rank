from __future__ import print_function, division
from grid import Grid
from itertools import permutations
import sys, re, time

move_list  = ['UP', 'DOWN', 'LEFT', 'RIGHT', 'CLEAN']
block_dict = {'bot': 'b', 'tile': '-', 'target': 'd'}
path = []

def next_move( r, c, grid ):
    global move_list
    global block_dict
    move = None

    # Find all dirty rooms. If none are found, you are done.
    dirty_rooms = find_ds(grid, block_dict['target'])
    if not dirty_rooms:
        return move

    dr = None
    if len(dirty_rooms) > 6:
        dr = sorted(dirty_rooms, key=lambda x: abs(x[0] - r) + abs(x[1] - c) )[0]
    else:
        dirty_rooms.insert(0, (r,c))
        mat = gen_adjacency_matrix( dirty_rooms )
        dr = get_shortest_path( dirty_rooms, mat )
        dr = dirty_rooms[dr[0]]

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

def get_shortest_path( dirty_rooms, mat ):
    total = -1
    path = []
    for n in permutations(list(range(1, len(dirty_rooms)))):
        curr_total = get_path_total( n, mat )
        if curr_total < total or total < 0:
            total = curr_total
            path = n
    return path

def get_path_total( path, mat ):
    total = mat[0][path[0]]
    # print('Path: ', path)
    if len(path) > 1:
        for n in range(len(path) - 1):
            # print('Logging:\tN: {}\tN+1: {}\tPath Length: {}\tMat: {}'.format(n, n+1, len(path), len(mat)))
            # print( mat[path[n]] )
            # print( mat[path[n]][path[n+1]] )

            total += mat[path[n]][path[n+1]]
    return total

def gen_adjacency_matrix( dirty_rooms ):
    mat = []
    for i in dirty_rooms:
        mat.append(list())
        for j in dirty_rooms:
            mat[-1].append( get_diff(i,j) )
    return mat

def get_diff( a, b ):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

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


# def find_ds( grid, string ):
#     """Finds all instances of string in the grid and returns indices."""
#     rows, columns = len(grid), len(grid[0])
#     print('Rows: {}\tColumns: {}'.format(rows, columns))
#     return [ (x.start()//rows, x.start()%columns) for x in re.finditer(string, ''.join(grid)) ]

def find_ds( grid, string ):
    """Finds all instances of string in the grid and returns indices."""
    rows, columns = len(grid), len(grid[0])
    ds = []
    for r in range(rows):
        for c in range(columns):
            if grid[r][c] == string:
                ds.append((r, c))
    return ds

def main():
    lines = sys.stdin.readlines()
    r, c  = [ int(x) for x in lines[0].split() ]
    h, w  = [ int(x) for x in lines[1].split() ]
    grid  = [ x.strip() for x in lines[2:] ]

    # print(next_move(r, c, grid))

    maze = Grid(r, c, grid)
    maze.start()
    wait_time = 0.05

    while True:
        movement = next_move(r, c, grid)
        if not movement:
            break

        r, c, grid = mod_grid( r, c, grid, movement )
        maze.set_grid_data( r, c, grid )
        # time.sleep( wait_time )

    time.sleep( wait_time )
    maze.close()

    print('\n'.join(grid))

if __name__ == '__main__':
    main()
