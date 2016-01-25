from __future__ import print_function
import sys

def day11(input_data):
    """Finds the largest hourglass sum."""
    largest = float('-inf')

    # Iterate through all possible hourglasses.
    for x in range(0, 4):
        for y in range(0, 4):

            # Calculate the total of the current hour glass.
            total = 0
            for point in get_hourglass(x, y):
                total += input_data[ point[1] ][ point[0] ]

            # If the current hourglass total is the largest thus far, update.
            if total > largest:
                largest = total

    return largest

def get_hourglass(x, y):
    """Returns the points of an hourglass starting at the origin point (x,y) at the upper left corner."""
    return [
        (x,   y),
        (x+1, y),
        (x+2, y),
        (x+1, y+1),
        (x,   y+2),
        (x+1, y+2),
        (x+2, y+2),
    ]

def main():
    input_data = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
    print(day11(input_data))

if __name__ == '__main__':
    main()
