from __future__ import print_function
import random

# Print the location of the bot, which is standardized to be the top left.
print(0, 0)

# Randomly generate the dimensions of the grid.
MIN_RANGE = 5
MAX_RANGE = 50
rows      = random.randint( MIN_RANGE, MAX_RANGE )
columns   = random.randint( MIN_RANGE, MAX_RANGE )
print(rows, columns)

# Randomly generate a grid of the appropriate size with random dirty rooms.
grid = []
for row in range(rows):
    grid.append(''.join([ random.choice('-d') for _ in range(columns) ]))

# Place the bot in the top left corner.
grid[0] = 'b' + grid[0][1:]
for n in grid:
    print( n )
