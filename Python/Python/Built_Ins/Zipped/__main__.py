from __future__ import print_function
import sys

def zippy(arr):
    return [sum(x) / len(x) for x in zip(*arr)]

def main():
    lines = [[float(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
    for num in zippy(lines[1:]):
        print(num)

if __name__ == '__main__':
    main()
