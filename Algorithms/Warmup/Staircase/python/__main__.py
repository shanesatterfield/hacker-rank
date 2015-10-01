from __future__ import print_function
import sys

def staircase(height):
    lines = []
    for n in range(height):
        string = ''
        for i in range(height):
            string += '#' if i >= n else ' '
        lines.append(string)
    return reversed(lines)

def main():
    T = int(input())
    for line in staircase(T):
        print(line)

if __name__ == '__main__':
    main()
