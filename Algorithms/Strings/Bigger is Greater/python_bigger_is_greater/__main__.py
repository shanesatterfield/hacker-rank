"""
Bigger is Greater
=================
Given a word w, rearrange the letters of w to construct another word s in such a way that s is lexicographically greater than w. In case of multiple possible answers, find the lexicographically smallest one.
"""
from __future__ import print_function, division, generators
import sys

def greater( string ):
    index, string = make_larger( string )
    if index >= 0:
        return string[:index+1] + make_smaller( string[index+1:] )
    else:
        return 'no answer'

def make_larger( string ):
    final_index = -1
    for n in range( len(string) )[:-1][::-1]:
        # Gets the indices of the characters that are candidates to be swapped.
        result = sorted([ index for index in range(n, n+len(string[n:])) if string[index] > string[n] ], key= lambda x: string[x])

        if len( result ) > 0:
            # The index of the character that you are making the swap with.
            final_index = n

            # The actual swapping code.
            char = string[n]
            index = result[0]
            string = string[:n] + string[index] + string[n+1:]
            string = string[:index] + char + string[index+1:]
            break

    return (final_index, string)

def make_smaller( string ):
    index = -1
    for n in range( len(string) )[:-1]:
        result = sorted([ index for index in range(n, n+len(string[n:])) if string[index] < string[n] ], key= lambda x: string[x])
        if len( result ) > 0:
            found = True
            char = string[n]
            index = result[0]
            string = string[:n] + string[index] + string[n+1:]
            string = string[:index] + char + string[index+1:]
    return string

def main():
    T = int(input())
    for line in sys.stdin.readlines()[:T]:
        print(greater(line.strip()))

if __name__ == '__main__':
    main()
