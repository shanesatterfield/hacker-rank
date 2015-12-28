from __future__ import print_function
import sys, re

def is_valid(re_str):
    try:
        re.compile(re_str)
        return True
    except re.error as e:
        return False

def main():
    T = int(input())
    lines = [line.strip() for line in sys.stdin.readlines()[:T]]
    for line in lines:
        print(is_valid(line))

if __name__ == '__main__':
    main()
