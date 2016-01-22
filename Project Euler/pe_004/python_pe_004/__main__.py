from __future__ import print_function
import sys

def pe_004(num):
    return num

def main():
    lines = [int(line) for line in sys.stdin.readlines()]
    for line in lines:
        print(pe_004(line))

if __name__ == '__main__':
    main()
