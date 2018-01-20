from __future__ import print_function
from functools import reduce
import sys, operator

def euler_008(K, arr):
    """Find the largest product of K consecutive items."""
    # Make sure that the types are correct.
    arr = list(map(int, arr))
    if type(K) is str:
        K = int(K)

    if K <= 0:
        return 0

    prev    = calculate_product(K, K, arr)
    largest = prev

    for i in range(K, len(arr)):
        if arr[i-K] == 0:
            prev = calculate_product(K-1, i, arr)
        else:
            curr = prev // arr[i-K]

        curr *= arr[i]
        print('prev: ', curr, prev, arr[i], arr[i-K])
        prev = curr
        if curr > largest:
            largest = curr

    return largest

def calculate_product(K, i, arr):
    return reduce(operator.mul, arr[i-K:i], 1)

def main():
    T = int(input())
    input_data = [[x for x in line.strip().split()] for line in sys.stdin.readlines()[:T*2]]

    for i in range(0, len(input_data), 2):
        print(euler_008(input_data[i][1], input_data[i+1][0]))

if __name__ == '__main__':
    main()
