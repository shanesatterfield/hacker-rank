"""
Alternating Strings
===================
Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.
"""
from __future__ import print_function, division, generators
import sys

def astr( string ):
    string = string.upper()

    count = 0
    for n in range( 1, len(string) ):
        if string[n] == string[n-1]:
            count += 1

    return count

def main():
    T = int(input())
    for line in sys.stdin.readlines()[:T]:
        print( astr( line ) )

if __name__ == '__main__':
    main()
