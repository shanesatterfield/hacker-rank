from __future__ import print_function
import sys, re

def resplit(text):
    return [ x for x in re.split(r'[,.]+', text) if len(x) > 0 ]

def main():
    for line in resplit(sys.stdin.read().rstrip()):
        print(line)

if __name__ == '__main__':
    main()
