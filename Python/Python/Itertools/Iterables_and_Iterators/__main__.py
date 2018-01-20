from __future__ import print_function, division
import sys, itertools

def iterab(arr, r):
    lst = list(itertools.combinations(arr, r))
    total_with = len(list(filter(lambda x: 'a' in x, lst)))
    total = len(lst)
    return total_with / total

def main():
    lines = sys.stdin.readlines()[:3]
    print(iterab(lines[1].strip().split(), int(lines[2])))

if __name__ == '__main__':
    main()
