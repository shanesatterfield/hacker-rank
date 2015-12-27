from __future__ import print_function, division
import sys

prefix = 'Error Code: '

def excerpt(a, b):
    try:
        return int(a) // int(b)
    except (ZeroDivisionError, ValueError) as e:
        return prefix + str(e)

def main():
    lines = [[x for x in line.strip().split()] for line in sys.stdin.readlines()[1:]]
    for line in lines:
        print(excerpt(*line[:2]))

if __name__ == '__main__':
    main()
