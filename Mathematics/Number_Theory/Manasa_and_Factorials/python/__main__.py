from __future__ import print_function, division
import sys, math

def manasa(N):
    result = 1
    zeroes = 0
    i = 1
    mod = int(math.pow(10, 10))
    while zeroes < N:
        i += 1
        # result = ((result%mod) * (i%mod))%mod
        ztmp, ntmp = zero_drop(i)
        zeroes += ztmp

        # result = result * ntmp
        result = ((result%mod) * (ntmp%mod))%mod
        ztmp, result = zero_drop(result)
        zeroes += ztmp
    return i

def zero_drop(num):
    # zeroes = 0
    # while num % 10 == 0 and num > 0:
    #     zeroes += 1
    #     num = num // 10
    # return zeroes, num
    temp = int(str(num).rstrip('0'))
    zeroes = num // temp // 10 # if temp != num else 0
    return zeroes, temp


def main():
    T = int(input())
    data = [int(x) for x in sys.stdin.read().strip().split()]

    for n in data:
        print(manasa(n))

if __name__ == '__main__':
    main()
