from __future__ import print_function, division
import sys

def reverse_game(N, K):
    N -= 1
    if K >= N // 2:
        return (N - K)*2
    return K*2 + 1

def main():
    T = int(input())
    lines = [[int(x) for x in line.strip().split()] for line in sys.stdin.readlines()[:T]]

    for line in lines:
        print(reverse_game(*line))

if __name__ == '__main__':
    main()
