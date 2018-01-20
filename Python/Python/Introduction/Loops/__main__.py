from __future__ import print_function
import sys

def loops(num):
    return [ x**2 for x in range(num) ]

def main():
    result = loops(int(input()))
    for line in result:
        print(line)

if __name__ == '__main__':
    main()
