from __future__ import print_function
from collections import Counter
import sys

def most_common(text):
    counter = Counter(text.lower())
    lst = [ (x[0], counter[x]) for x in counter ]

    # Sort first by the count and then by the key. Flip to negative for inverse.
    return sorted(lst, key=lambda x: (-x[1], x[0]))[:3]

def main():
    # Parse input and process it.
    result = most_common(sys.stdin.read().strip())

    # Print proper output.
    for x in result:
        print(x[0], x[1])

if __name__ == '__main__':
    main()
