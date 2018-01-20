from __future__ import print_function
import sys

def defaultdict(arr, key):
    diction = dict()
    for k in key:
        diction[k] = []

    for i in range(len(arr)):
        if arr[i] in diction:
            diction[arr[i]].append(i+1)

    result = []
    for x in key:
        curr = diction[x]
        if len(curr) == 0:
            curr = [-1]
        result.append(curr)

    return result

def main():
    lines = sys.stdin.readlines()
    config = [int(x) for x in lines[0].strip().split()]
    lines = [ x.strip() for x in lines[1:] ]
    for line in defaultdict(lines[:config[0]], lines[config[0]:]):
        print(*line)

if __name__ == '__main__':
    main()
