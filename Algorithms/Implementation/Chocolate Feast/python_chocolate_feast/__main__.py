from __future__ import print_function, division

import sys

def main():
    T = int(input())
    for line in sys.stdin.readlines()[:T]:
        args = [ int(x) for x in line.split() ]
        print(feast( args[0], args[1], args[2] ))

def feast( N, C, M ):
    count = 0
    temp_count = N // C
    while True:
        free_choco = temp_count + (count % M)
        count += temp_count

        if free_choco < M:
            break

        temp_count = free_choco // M

    return count

if __name__ == '__main__':
    main()
