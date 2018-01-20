from __future__ import print_function
import sys

def nested( lst ):
    ans = {}
    for n in lst:
        if n[1] not in ans:
            ans[n[1]] = []
        ans[n[1]].append(n[0])
    return sorted(ans[sorted(ans.keys())[1]])

def main():
    T = int(input())
    lines = [ x.strip() for x in sys.stdin.readlines()[:T*2] ]
    lst = [ [lines[x], float(lines[x+1])] for x in range(0, len(lines), 2) ]
    for n in nested(lst):
        print(n)

if __name__ == '__main__':
    main()
