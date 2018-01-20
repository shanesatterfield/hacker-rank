from __future__ import print_function
import sys

def day10(num):
    arr = []
    while num > 0:
        c     = chr(ord('0') + int(num & 1))
        num >>= 1
        arr.append(c)
    return ''.join(list(reversed(arr)))

def main():
    T = int(input())
    lines = [ int(line.strip()) for line in sys.stdin.readlines()[:T]]
    for line in lines:
        print(day10(line))

if __name__ == '__main__':
    main()
