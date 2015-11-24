from __future__ import print_function, division
import sys

# Determines the index that should be removed from a string to make it a palindrome.
# Assumes there is a solution.
# Returns -1 if the string is already a palindrome.
def mkpal(string):
    index       = -1
    max_index   = len(string)-1
    first_half  = (len(string)-1) // 2
    second_half = max_index - first_half

    for i in range(len(string)):
        if string[i] != string[max_index - i]:
            index = i if is_palindrome(string[:i] + string[i+1:]) else max_index - i
            break

    return index

def is_palindrome(string):
    result = True
    max_index = len(string)-1

    for i in range(len(string)):
        if string[i] != string[max_index - i]:
            result = False
            break

    return result

def main():
    T = int(input())
    lines = [ x.strip() for x in sys.stdin.readlines() ]

    for line in lines:
        print(mkpal(line))

if __name__ == '__main__':
    main()
