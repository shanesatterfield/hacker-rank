from __future__ import print_function, division
import sys

# Bit flip technique
def manasa(N, a, b):
    ans = {a, b}
    for n in range(N-2):
        temp = set()
        for n in ans:
            temp.add(n+a)
            temp.add(n+b)
        ans = temp
    return sorted(list(ans))

def main():
    T = int(input())
    lines = sys.stdin.readlines()[:T*3]
    for i in range(T):
        N, a, b = [ int(x.strip()) for x in lines[i*3:(i+1)*3] ]
        print(*manasa(N, a, b))

if __name__ == '__main__':
    main()

# Note: These were far too slow and inefficient, but they were functional.

# from functools import reduce
# Recursion
# def manasa(N, a, b):
#     return sorted(list(manasa_recursive(N-1, a, b, [])))
#
# def manasa_recursive(N, a, b, lst):
#     if len(lst) >= N:
#         return set([reduce(lambda x, y: x+y, lst)])
#     else:
#         ans = set()
#         ans.update(manasa_recursive(N, a, b, lst+[a]))
#         ans.update(manasa_recursive(N, a, b, lst+[b]))
#         return ans

# List generations
# def manasa(N, a, b):
#     lst = [[a], [b]]
#     for _ in range(N-2):
#         temp = []
#         for n in lst:
#             temp.append(n + [a])
#             temp.append(n + [b])
#         lst = temp
#
#     ans = set()
#     for n in lst:
#         ans.add(reduce(lambda x,y: x+y, n))
#
#     return sorted(list(ans))
