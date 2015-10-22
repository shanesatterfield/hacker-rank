from __future__ import print_function
import sys, itertools

def perms(string, size):
    return sorted([ ''.join(x) for x in list(itertools.permutations(string, size)) ])

def main():
    string, size = sys.stdin.read().split()
    for line in perms(string, int(size)):
        print(line)

if __name__ == '__main__':
    main()
