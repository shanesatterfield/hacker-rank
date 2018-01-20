from __future__ import print_function
import sys

def to_anagram( a, b ):
    a = a.lower()
    b = b.lower()

    # Finds out how many of each letter is in each of the strings.
    mymaps = ( count(a), count(b) )

    # The minimum number of deletions necessary.
    deletion_count = 0

    # Loops through the maps of letter counts. Goes from string a to b.
    for curr in range(len(mymaps)):

        # Goes through each letter in the map.
        for n in mymaps[curr]:
            if n not in mymaps[flip(curr)]:
                deletion_count += mymaps[curr][n]
            else:
                deletion_count += abs(mymaps[curr][n] - mymaps[flip(curr)][n])
                del mymaps[flip(curr)][n]

    return deletion_count

# Takes an integer index of either 0 or 1 and returns the other index.
def flip( index ):
    return abs(index-1)

# Counts the occurances of letters in the given string.
def count( string ):
    letters = dict()
    for letter in string:
        if letter not in letters:
            letters[letter] = 0
        letters[letter] += 1
    return letters

def main():
    print(to_anagram(*[ x.strip() for x in sys.stdin.readlines()[:2] ]))

if __name__ == '__main__':
    main()
