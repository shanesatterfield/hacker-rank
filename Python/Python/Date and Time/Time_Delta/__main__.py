from __future__ import print_function
import sys
from datetime import datetime

time_format = '%a %d %b %Y %H:%M:%S %z';

def delta(time1, time2):
    a = datetime.strptime(time1, time_format)
    b = datetime.strptime(time2, time_format)

    return abs(int((a - b).total_seconds()))


def main():
    T = int(input())
    lines = [x.strip() for x in sys.stdin.readlines()[:T*2]]

    for i in range(T):
        print(delta(lines[i*2], lines[i*2 + 1]))


if __name__ == '__main__':
    main()
