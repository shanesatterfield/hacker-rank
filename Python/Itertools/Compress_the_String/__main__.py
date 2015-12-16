from __future__ import print_function
import sys, itertools

def compress(text):
    return list(map(groupit, itertools.groupby(map(int, text))))

def groupit(obj):
    temp = list(obj[1])
    return (len(temp), temp[0])

def main():
    print(*compress(sys.stdin.read().strip()))

if __name__ == '__main__':
    main()
