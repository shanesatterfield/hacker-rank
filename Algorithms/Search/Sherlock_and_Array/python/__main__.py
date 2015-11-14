from __future__ import print_function
import sys

def sherlock(arr):
    if len(arr) == 1: return True

    left = 0
    right = sum(arr)
    result = False

    for n in arr:
        right -= n
        if left == right:
            result = True
            break
        left += n

    return result

def main():
    lines = [ [int(b) for b in x.strip().split()] for x in sys.stdin.readlines()[2::2] ]
    for line in lines:
        print("YES" if sherlock(line) else "NO")

if __name__ == '__main__':
    main()
