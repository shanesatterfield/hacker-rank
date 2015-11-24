from __future__ import print_function
import sys, itertools

def manasa(num):
    result = False
    # for n in filter(itertools.permutations(str(num)), ):
    #     if ord(n[-1]) & 1 == 0 and int(''.join(n)) % 8 == 0:
    #         result = True
    #         break
    return result

def main():
    T = int(input())
    lines = [ int(x) for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print('YES' if manasa(line) else 'NO')

if __name__ == '__main__':
    main()
