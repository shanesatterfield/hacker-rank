from __future__ import print_function
import sys

def diagonally(mat):
    total = 0
    for i in range(len(mat)):
        total += mat[i][i] - mat[len(mat)-1-i][i]
    return abs(total)

def main():
    T = int(input())
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()]

    print(diagonally(lines))

if __name__ == '__main__':
    main()
