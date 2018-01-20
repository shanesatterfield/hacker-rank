from __future__ import print_function
import sys, re

def count_subs( text, substring ):
    count = 0
    for n in range( len(text) - len(substring) + 1 ):
        if text[n:n+len(substring)] == substring:
            count += 1
    return count

def main():
    text, substring = [ x.strip() for x in sys.stdin.readlines()[:2] ]
    print( count_subs( text, substring ) )

if __name__ == '__main__':
    main()
