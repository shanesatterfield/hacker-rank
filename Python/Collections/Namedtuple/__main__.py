from __future__ import print_function, division
import sys, collections

def ntup(input_data):
    """Finds the average marks of the class."""
    # Creates the named tuple.
    Row = collections.namedtuple('Row', ','.join(input_data[1]))

    # Collect all marks from the input data.
    rows = []
    for line in input_data[2:]:
        rows.append(Row(*line).MARKS)

    # Calculates the averge marks.
    result = sum(map(int, rows)) / len(rows)

    # Return the answer as a formatted string.
    return '{0:.2f}'.format(result)

def main():
    lines = [line.strip().split() for line in sys.stdin.readlines()]
    print(ntup(lines))

if __name__ == '__main__':
    main()
