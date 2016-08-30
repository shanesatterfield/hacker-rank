from __future__ import print_function
from cmath import *
import sys, re

def parse_input():
    input_data = sys.stdin.read().rstrip()
    input_data = re.match(r'(\-{0,1}[0-9]+)\+{0,1}(\-{0,1}[0-9]+)j', input_data).groups()
    return [ int(x) for x in input_data ]

def get_phi(x, y):
    return phase(complex(x, y))

def get_r(x, y):
    return abs(complex(x, y))

def main():
    nums = parse_input()
    print(get_r(*nums))
    print(get_phi(*nums))

if __name__ == '__main__':
    main()
