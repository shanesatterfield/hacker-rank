from __future__ import print_function
import sys, re

def valphone(text):
    return re.match(r'^[789][0-9]{9}$', text) != None

def main():
    T = int(input())
    lines = sys.stdin.readlines()[:T]
    for line in lines:
        print("YES" if valphone(line) else "NO")

if __name__ == '__main__':
    main()
