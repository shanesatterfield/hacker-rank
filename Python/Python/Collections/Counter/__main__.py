from __future__ import print_function
from collections import Counter
import sys

def count(sizes, customers):
    counter = Counter(sizes)

    earnings = 0
    for cust in customers:
        if cust[0] in counter and counter[cust[0]] > 0:
            counter.subtract({cust[0]: 1})
            earnings += cust[1]
    return earnings



def main():
    X = int(input())
    lines = sys.stdin.readlines()
    sizes = [ int(x.strip()) for x in lines[0].split() ]

    N = int(lines[1].strip())
    customers = [ [int(i) for i in x.split()] for x in lines[2:] ]
    print(count(sizes, customers))

if __name__ == '__main__':
    main()
