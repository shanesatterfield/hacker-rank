"""
Sherlock and The Beast

Problem Statement
Sherlock Holmes is getting paranoid about Professor Moriarty, his arch-enemy. All his efforts to subdue Moriarty have been in vain. These days Sherlock is working on a problem with Dr. Watson. Watson mentioned that the CIA has been facing weird problems with their supercomputer, 'The Beast', recently.

This afternoon, Sherlock received a note from Moriarty, saying that he has infected 'The Beast' with a virus. Moreover, the note had the number N printed on it. After doing some calculations, Sherlock figured out that the key to remove the virus is the largest Decent Number having N digits.

A Decent Number has the following properties:

1. 3, 5, or both as its digits. No other digit is allowed.
2. Number of times 3 appears is divisible by 5.
3. Number of times 5 appears is divisible by 3.

Meanwhile, the counter to the destruction of 'The Beast' is running very fast. Can you save 'The Beast', and find the key before Sherlock?
"""

from __future__ import print_function, division

import sys, math

def main():
    # Get the number of tests to run.
    T = int(input())
    for n in range( T ):
        N = int(input())
        print( get_decent( N ) )

def get_decent( N ):
    original = N
    fives = 0
    threes = 0

    if N < 3:
        return -1

    # Calculate the number of fives. Has to be divisible by 3.
    fives = N // 3
    N %= 3

    # Calculate the number of threes. Has to be divisible by 5.
    threes = N // 5
    N %= 5

    # If the remainder is two, then swap a five for a three to even out.
    while N > 0 and fives > 0 and N <= original:
        N += 3
        fives  -= 1

        if N % 5 == 0:
            threes += N // 5
            N %= 5

    if (fives <= 0 and threes <= 0) or N > 0:
        return -1

    return int(("555" * fives) + ("33333" * threes))

# This produces a runtime error this larger values.
def gen_number( N, fives, threes ):
    num = 0
    for i in range( fives ):
        num += 555 * math.pow( 10, N-3 )
        N -= 3

    for i in range( threes ):
        num += 33333 * math.pow( 10, N-5 )
        N -= 5

    return int(num)


if __name__ == '__main__':
    main()
