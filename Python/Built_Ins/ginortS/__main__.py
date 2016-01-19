from __future__ import print_function, division
import sys, functools

def sort_key(c):
    if c.islower():
        return ord(c) - ord('a')
    elif c.isupper():
        return ord(c) - ord('A') + ord('z')
    elif c.isdigit():
        offset = ord('Z') + ord('z')
        curr   = ord(c) - ord('0')
        if curr % 2 != 0:
            return offset + curr // 2
        else:
            return offset + curr // 2 + 5

def ginorts(string):
    return functools.reduce(lambda x,y: x + y, sorted(string, key=sort_key))

def main():
    print(ginorts(sys.stdin.read().strip()))

if __name__ == '__main__':
    main()
