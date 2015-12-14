from __future__ import print_function
import sys

def issub(a, b):
    return set(a).issubset(set(b))

def main():
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()]
    for i in range(lines[0][0]):
        print(issub(lines[2 + 4*i], lines[4 + 4*i]))

if __name__ == '__main__':
    main()

#####################
# Condensed Version #
#####################
# import sys
# lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()[2::2]]
# for i in range(0, len(lines), 2): print(set(lines[i]).issubset(set(lines[i+1])))
