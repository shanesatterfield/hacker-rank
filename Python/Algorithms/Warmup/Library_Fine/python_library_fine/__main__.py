from __future__ import print_function
import sys

def fine(actual, expected):
    total = 0
    if expected[2] == actual[2] and expected[1] == actual[1]:
            total = max(0,  15 * (actual[0] - expected[0]))
            
    elif expected[2] == actual[2] and expected[1] < actual[1]:
            total = max(0, 500 * (actual[1] - expected[1]))

    elif expected[2] < actual[2]:
        total = 10000

    return total

def main():
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()[:2]]
    print(fine(*lines))

if __name__ == '__main__':
    main()
