from __future__ import print_function
import sys

def got( word ):
    word = word.lower()
    letters = dict()
    for n in word:
        if n not in letters:
            letters[n] = 0
        letters[n] += 1

    arr = list(letters.values())

    if len(word) % 2 == 0:
        return all( x % 2 == 0 for x in arr )
    else:
        return [ x % 2 == 0 for x in arr ].count(False) == 1


def main():
    print('YES' if got(sys.stdin.read().strip()) else 'NO')

if __name__ == '__main__':
    main()
