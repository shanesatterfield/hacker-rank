from __future__ import print_function, division

import sys

# Searches the grid G and returns True if P is found within G.
def grid_search( G, P ):
    grid = get_search_area( G, P )

    result = False
    for j in range( len(grid) ):
        for i in range( len(grid[0]) ):
            if( grid[j][i] == P[0][0] ) and check_block( i, j, G, P ):
                result = True
                break

    return result

# Checks to see if P starts at the given location of grid G.
def check_block( cols, rows, G, P ):
    result = True
    for j in range( rows, rows + len(P) ):
        line = G[j][cols: cols + len(P[0])]
        if line != P[j-rows]:
            result = False
            break

    return result

# Crops the grid G to only the area that should be searched for the first character in pattern P.
def get_search_area( G, P ):
    g_dims = [ len(G[0]), len(G) ]
    p_dims = [ len(P[0]), len(P) ]

    return [ x[:(g_dims[0] - p_dims[0] + 1)] for x in G[:(g_dims[1] - p_dims[1] +1)] ]

# Returns the block when given the stdin input. For ease of use.
def get_block( string, starting_index ):
    dims = [ int(x) for x in string[starting_index].split() ]
    starting_index += 1
    G = [ x[:dims[1]] for x in string[ starting_index: starting_index+dims[0] ] ]
    return [ G, starting_index + dims[0] ]

# Handles stdin input, runs the code and prints the proper output to stdout.
def main():
    T = int(input())
    data = sys.stdin.readlines()
    index = 0
    for n in range( T ):
        temp = get_block( data, index )
        G = temp[0]
        index = temp[1]

        temp = get_block( data, index )
        P = temp[0]
        index = temp[1]

        if grid_search( G, P ):
            print('YES')
        else:
            print('NO')

if __name__ == '__main__':
    main()
