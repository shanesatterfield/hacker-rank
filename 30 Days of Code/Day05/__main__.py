from __future__ import print_function
import sys, math

def day05(a, b, n):
    prev = a
    curr = 0
    for i in range(0, n):
        curr = prev + int(math.pow(2, i)) * b
        prev = curr
        yield curr

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()][1:]
    for line in lines:
        print(*list(day05(*line)))

if __name__ == '__main__':
    main()
