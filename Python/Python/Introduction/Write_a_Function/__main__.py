from __future__ import print_function, division
import sys

def is_leap(year):
    return (year % 400 == 0) or (year % 100 != 0) and (year % 4 == 0)

def main():
    year = int(sys.stdin.read().strip())
    print(is_leap(year))

if __name__ == '__main__':
    main()
