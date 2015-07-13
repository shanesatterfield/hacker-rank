"""
Song of Pi

Problem Statement

Today is a special day, and let me sing a song to celebrate the day:

    "Now, I wish I could recollect pi.
    'Eureka,' cried the great inventor.
    Christmas Pudding, Christmas Pie
    Is the problem's very center."

Well, you may say it's a terrible song - but it's not! Ignore the punctuation marks and write down the length of each of word in this song.

For example:

    "Now"=3, "I"=1, "wish"=4, etc etc

Writing them together we get:
314159265358979323846

That's the value of pi! (Ignoring the floating point) A song is a pi song if the length of its words represent the value of pi.

Today, March 14, is the official Pi Day because 3/14 represents the first three significant digits of Pi. And today you will determine which songs are pi songs and which are not.

Assume that value of pi is 3.1415926535897932384626433833. You don't need more digits for this problem; use the value exactly as it is, just ignore the floating point and don't perform any rounding operations.
"""

from __future__ import print_function, division

import sys, re

MY_PI = '31415926535897932384626433833'

def main():
    T = int(input())
    for n in range( T ):
        text = str(input())

        if is_pi_song( text ):
            print("It's a pi song.")
        else:
            print("It's not a pi song.")

def is_pi_song( song ):
    result = True
    words = get_words( song )

    for n in range(len(words)):
        if len( words[n] )!= int( MY_PI[n] ):
            result = False
            break

    return result


def get_words( text ):
    return re.sub(r'\W+', ' ', text).split()

if __name__ == '__main__':
    main()
