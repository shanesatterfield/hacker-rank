from __future__ import print_function
import sys

def day07(arr):
    return list(reversed(arr))

def main():
    T = int(input())
    input_data = [int(x) for x in sys.stdin.read().strip().split()]
    print(*day07(input_data))

if __name__ == '__main__':
    main()
