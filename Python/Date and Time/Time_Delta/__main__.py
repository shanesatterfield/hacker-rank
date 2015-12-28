from __future__ import print_function
import sys, datetime

def delta(time1, time2):
    return datetime.datetime.utcfromtimestamp(time1)

def main():
    T = int(input())
    lines = [x.strip() for x in sys.stdin.readlines()[:T*2]]

    for i in range(T):
        print(delta(lines[i*2], lines[i*2 + 1]))


if __name__ == '__main__':
    main()
