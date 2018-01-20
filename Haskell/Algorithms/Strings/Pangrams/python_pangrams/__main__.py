"""
Pangrams
========
Roy wanted to increase his typing speed for programming contests. So, his friend advised him to type the sentence "The quick brown fox jumps over the lazy dog" repeatedly, because it is a pangram. (Pangrams are sentences constructed by using every letter of the alphabet at least once.)

After typing the sentence several times, Roy became bored with it. So he started to look for other pangrams.

Given a sentence s, tell Roy if it is a pangram or not.
"""
from __future__ import print_function, division

import sys, re

def is_pangram( text ):
    return len(set(sorted(re.sub(r'[^a-z]+', '', text.lower())))) == 26

def main():
    for text in sys.stdin.readlines():
        if not is_pangram( text ):
            print('not ', end="")

        print('pangram')

if __name__ == '__main__':
    main()
