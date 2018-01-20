from __future__ import print_function
import sys

def day06(n, c='#'):
    lines = []
    for i in range(1, n+1):
        # Creates the string by multiplying the character and padding spaces to the left.
        curr = (c*(i)).rjust(n)
        lines.append(curr)
    return lines

def main():
    n = int(input())
    for line in day06(n):
        print(line)
        
if __name__ == '__main__':
    main()
