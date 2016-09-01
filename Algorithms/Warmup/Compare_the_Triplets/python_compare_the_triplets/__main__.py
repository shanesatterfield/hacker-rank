from __future__ import print_function
import sys

def score(alice, bob):
    matches = [ [ int(a > b), int(a < b) ] for a, b in zip(alice, bob) ]
    return [ sum(x) for x in zip(*matches) ]

def give_point(a, b):
    return [ int(a > b), int(a < b) ]

def main():
    input_data = [ [ int(x) for x in line.strip().split() ] for line in sys.stdin.readlines() ]
    print(*score(input_data[0], input_data[1]))

if __name__ == '__main__':
    main()
