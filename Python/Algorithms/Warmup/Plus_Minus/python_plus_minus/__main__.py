from __future__ import print_function, division
import sys

def pm(nums):
    pos, neg, zero = 0, 0, 0
    for n in nums:
        if n > 0:
            pos += 1
        elif n < 0:
            neg += 1
        else:
            zero += 1
    return [round(pos/len(nums),3), round(neg/len(nums),3), round(zero/len(nums),3)]

def main():
    T = int(input())
    nums = [int(x) for x in sys.stdin.read().strip().split()]

    for n in pm(nums):
        print('{0:.3f}'.format(n))

if __name__ == '__main__':
    main()
