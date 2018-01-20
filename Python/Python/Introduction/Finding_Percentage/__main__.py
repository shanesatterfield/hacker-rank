from __future__ import print_function, division
import sys

students = dict()

def percentage_store(lines):
    for line in lines:
        students[line[0]] = sum(map(float, line[1:])) / len(line[1:])

def finding(name):
    return '{0:.2f}'.format(students[name])

def main():
    T = int(input())
    lines = [ line.strip().split() for line in sys.stdin.readlines() ]
    percentage_store(lines[:T])

    # Prints the final name
    print(finding(lines[T][0]))

if __name__ == '__main__':
    main()
