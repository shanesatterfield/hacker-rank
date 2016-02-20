from __future__ import print_function, division
import sys

def handshakes(people):
    if people <= 0:
        return 0
    return people * (people-1) // 2

def main():
    T = int(input())
    input_data = [int(x) for x in sys.stdin.readlines()[:T]]

    for line in input_data:
        print(handshakes(line))

if __name__ == '__main__':
    main()
