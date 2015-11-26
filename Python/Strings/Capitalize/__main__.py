from __future__ import print_function
import sys, re

def capitalize(text):
    return ''.join([ x[0].upper() + x[1:] if x.isalpha() else x for x in re.split('(\W+)', text) ])

def main():
    print(capitalize(sys.stdin.read().rstrip()))

if __name__ == '__main__':
    main()
