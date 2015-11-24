from __future__ import print_function, division
import sys, math

# Modified cubic formula solution.
# Rounds for floating point error.
def ashish(candies):
    p = -0.5
    q = 1.5*candies
    r = 1/6

    g = math.pow((q**2) + math.pow(r-(p**2), 3), 1/2)
    x = math.pow(q + g, 1/3) + math.pow(q - g, 1/3) + p
    return int(round(x, 8))

# a=1/3, b=1/2, c=1/6 d=-candies
def cubic_forumla(a, b, c, d):
    p = -b/(3*a)
    q = (p**3) + (b*c - 3*a*d)/(6*(a**2))
    r = c/(3*a)

    g = math.pow((q**2) + math.pow(r-(p**2), 3), 1/2)
    x = math.pow(q + g, 1/3) + math.pow(q - g, 1/3) + p
    return int(round(x, 12))

def main():
    T = int(input())
    lines = [int(x.strip()) for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print(ashish(line))

if __name__ == '__main__':
    main()
