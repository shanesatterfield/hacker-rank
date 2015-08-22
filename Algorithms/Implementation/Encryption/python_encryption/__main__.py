from __future__ import print_function, division
import sys, math

def encryption( text ):
    length_sqrt = math.sqrt(len(text))
    row, column = int(math.floor(length_sqrt)), int(math.ceil(length_sqrt))
    if row * column < len(text):
        row += 1

    grid = [ list(text[x*column : (x+1)*column]) for x in range(row) ]

    result = []
    for x in range(column):
        string = ''
        for y in range(row):
            if x < len(grid[y]):
                string = string + grid[y][x]
        result.append(string)

    return ' '.join(result)

def main():
    lines = [ x.strip() for x in sys.stdin.readlines() ]
    for line in lines:
        print(encryption(line))

if __name__ == '__main__':
    main()
