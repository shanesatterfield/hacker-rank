from __future__ import print_function, division
import sys, math

def ashish(candies):
    # return ashish_naive(candies)
    return other_equ(candies)

def ashish_faster(candies):
    i = 0
    while True:
        if sqrs_seq(i+1) > candies:
            break
        i += 1
    return i

def sqrs_seq(x):
    return int((x/6) * (x+1) * (2*x + 1))

def other_equ(d):
    q = 1/36
    r = -27*(-d) + 0.5
    discriminant = math.pow(q,3) + math.pow(r,2)
    t = r - math.sqrt(discriminant)
    s = r + math.sqrt(discriminant)

    term1 = None
    if discriminant > 0:
        term1 = 1/6
    else:
        term1 = math.sqrt(3) * ((-t + s) / 2)
    r13 = 2 * math.sqrt(q)
    print(r13, q, q**3, r13*math.cos(math.pow(q,3)/3))
    return -term1 + r13*math.cos(math.pow(q,3)/3)

def ashish_naive(candies):
    i    = 0
    curr = None
    while True:
        curr = int(math.pow(i+1, 2))
        if curr > candies:
            break

        candies -= curr
        i += 1
    return i

def binary_search_start(num, full_range):
    return binary_search(num, full_range//2, full_range)

# Modified binary search for this problem.
def binary_search( num, curr, incr ):
    incr = incr // 2
    if num >= curr and num < curr+1:
        return curr
    elif curr > 0 and num >= curr-1
    if incr <= 0:
        if
    elif num > curr:
        return binary_search(num, curr - incr, incr)
    elif num < curr:
        return binary_search(num, curr + incr, incr)

def main():
    T = int(input())
    lines = [int(x.strip()) for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print(ashish(line))

if __name__ == '__main__':
    main()
