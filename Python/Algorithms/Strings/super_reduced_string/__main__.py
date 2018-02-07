import sys


def super_reduce_string(text: str) -> str:
    """
    Reduce a string by removing adjacent pairs of characters.
    """
    result = []

    for c in text:
        if len(result) == 0 or result[-1] != c:
            result.append(c)
        else:
            result.pop()

    return ''.join(result) or 'Empty String'


def main():
    """
    Solution for Algorithms -> Strings -> Super Reduced String

    Steve has a string, s, consisting of n lowercase English alphabetic
    letters. In one operation, he can delete any pair of adjacent letters with
    same value. For example, string "aabcc" would become either "aab" or "bcc"
    after operation.

    Steve wants to reduce s as much as possible. To do this, he will repeat the
    above operation as many times as it can be performed. Help Steve out by
    finding and printing s's non-reducible form!

    Note: If the final string is empty, print "Empty String".
    """
    text = sys.stdin.read().strip()
    print(super_reduce_string(text))


if __name__ == '__main__':
    main()
