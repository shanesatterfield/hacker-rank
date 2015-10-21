from __future__ import print_function
import sys, itertools

def combs(string, r):
    result = list()
    for n in range(1, r+1):
        result.extend(sorted([''.join(sorted(x)) for x in itertools.combinations(string, n)]))
    return result

def main():
    data = sys.stdin.read().split()
    for line in combs(data[0], int(data[1])):
        print(line)

if __name__ == '__main__':
    main()
