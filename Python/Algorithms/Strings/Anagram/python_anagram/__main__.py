from __future__ import print_function, division
from collections import Counter
import sys

def anagram(text):
    if len(text) & 1 == 1:
        return -1

    count_1 = Counter(text[len(text)//2:])
    count_2 = Counter(text[:len(text)//2])

    result = 0
    for key in count_1.keys():
        if key in count_2:
            result += min(count_1[key], count_2[key])

    return len(text)//2 - result

# Shortened version of the above anagram function.
def anagram_short(text):
    if len(text) & 1 == 1: return -1
    count_1, count_2 = Counter(text[len(text)//2:]), Counter(text[:len(text)//2])
    return len(text)//2 - sum([ min(count_1[key], count_2[key]) if key in count_2 else 0 for key in count_1.keys() ])

def main():
    T = int(input())
    lines = [x.strip() for x in sys.stdin.readlines()[:T]]

    for line in lines:
        print(anagram(line))

if __name__ == '__main__':
    main()
