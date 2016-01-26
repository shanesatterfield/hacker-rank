from __future__ import print_function
import sys, collections

def ordered_insert(input_data):
    od = collections.OrderedDict()

    # Insert values into the ordered dictionary
    for line in input_data:
        if line not in od:
            od[line] = 0
        od[line] = od[line] + 1

    # Calculate the net price.
    return [ (k[0], k[1] * v) for k,v in od.items() ]

def main():
    # Parse the input from stdin
    lines = [line.strip().split(' ') for line in sys.stdin.readlines()][1:]
    lines = list(map(lambda x: (' '.join(x[:-1]), int(x[-1])), lines))

    # Proper output
    for k, v in ordered_insert(lines):
        print(k, v)

if __name__ == '__main__':
    main()
