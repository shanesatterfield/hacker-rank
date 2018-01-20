from __future__ import print_function
import sys, itertools

def combs(string, num):
    return sorted([ ''.join(sorted(x)) for x in itertools.combinations_with_replacement(string, num)])

def main():
    string, num = sys.stdin.read().strip().split()
    for line in combs(string, int(num)):
        print(line)

if __name__ == '__main__':
    main()
