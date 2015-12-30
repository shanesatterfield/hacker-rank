from __future__ import print_function
import sys

def all_or_nothing(nums):
    return all(map(is_pos, nums)) and any(map(is_palindrome, nums))

def is_pos(num):
    return num >= 0

def is_palindrome(num):
    num = str(num)
    return num == ''.join(list(reversed(num)))

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
    print(all_or_nothing(lines[1]))

if __name__ == '__main__':
    main()
