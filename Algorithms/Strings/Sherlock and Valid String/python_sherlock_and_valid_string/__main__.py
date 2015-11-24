from __future__ import print_function, division
from collections import Counter
import sys

def sherlock(string):
    count = sorted(Counter(string).values())
    max_count = 1

    i, j = 0, len(count) - 1
    while i < j and count[i] != count[j] and max_count >= 0:
        diff = abs(count[i] - count[j])

        # If you can drop the value to zero, do so.
        if diff >= max_count and count[i] == 1:
            max_count -= 1
            i += 1

        # Else subtract the diff and move on.
        else:
            max_count -= diff
            i, j = i+1, j-1

    return max_count >= 0

def main():
    print("YES" if sherlock(sys.stdin.read().rstrip()) else "NO")

if __name__ == '__main__':
    main()
