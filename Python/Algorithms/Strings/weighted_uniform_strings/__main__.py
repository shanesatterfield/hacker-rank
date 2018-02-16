import sys
from typing import Set


def calculate_weights(text: str) -> Set[int]:
    """
    Build list of weights that can be found in the string.
    """
    splitted = split_text(text)
    weights = set()

    for s in splitted:
        weight = get_weight(s[0])
        for n in range(1, len(s) + 1):
            weights.add(weight * n)

    return weights


def split_text(text: str) -> Set[str]:
    """
    Split text into contiguous substrings of duplicate characters.
    """
    result = []
    for c in text:
        if result and c is not result[-1]:
            result.append(' ')
        result.append(c)

    return set(''.join(result).split())


def get_weight(c: str) -> int:
    """
    Calculate the weighted value of character c.
    """
    return ord(c.lower()) - ord('a') + 1


def main():
    """
    Solution for Algorithms -> Strings -> Weighted Uniform Strings.
    """
    lines = [line.strip() for line in sys.stdin.readlines()]
    text = lines[0]
    N = int(lines[1])
    queries = lines[2:N+2]
    weights = calculate_weights(text)

    for query in queries:
        print('Yes' if int(query) in weights else 'No')


if __name__ == '__main__':
    main()
