from __future__ import print_function
import sys, itertools

def get_sum(nums, M):
    """ Get the sum of a line. """
    return sum(map(lambda x: x**2, nums)) % M


def get_input():
    """ Parses input from stdin. """
    lines = [ map(int, x.rstrip().split()) for x in sys.stdin.readlines() ]
    K, M = lines[0]
    lines = process_lines(lines[1:], M)
    return K, M, lines


def process_lines(lines, M):
    """ Takes a line and mods each of the elements. """
    return [ list(set(map(lambda x: x % M, list(line)[1:]))) for line in lines ]


def find_largest(nums, M):
    # Get all combinations
    items = itertools.product(*nums)

    # Get the largest
    return max(get_sum(item, M) for item in items)


def main():
    # Parse the input from stdin
    K, M, lines = get_input()
    print(find_largest(lines, M))

if __name__ == '__main__':
    main()
