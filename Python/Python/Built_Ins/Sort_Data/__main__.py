from __future__ import print_function
import sys

def sort_data(arr, i):
    return sorted(arr, key=lambda x: x[i])

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
    for row in sort_data(lines[1:-1], lines[-1][0]):
        print(*row)

if __name__ == '__main__':
    main()
