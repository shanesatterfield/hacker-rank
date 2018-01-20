from __future__ import print_function
import sys, re

def isFloat(text):
    return True if re.match(r'^([+-]{0,1}[0-9]*\.)[0-9]+$', text) else False

def main():
    T = int(input())
    for line in sys.stdin.readlines()[:T]:
        print(isFloat(line))

if __name__ == '__main__':
    main()
