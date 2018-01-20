from __future__ import print_function
import sys

diction = dict()

def day08(diction, name):
    if name not in diction:
        return 'Not found'
    return '{}={}'.format(name, diction[name])

def main():
    T = int(input())
    lines = [line.strip() for line in sys.stdin.readlines()]
    for i in range(0, T*2, 2):
        diction[lines[i]] = lines[i+1]

    for line in lines[T*2:]:
        print(day08(diction, line))

if __name__ == '__main__':
    main()
