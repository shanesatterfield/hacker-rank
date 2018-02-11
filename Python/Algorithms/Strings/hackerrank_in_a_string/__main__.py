import sys
from collections import deque


def contains_hackerrank(text: str) -> bool:
    """
    Determines if a string contains a subsequence of 'hackerrank'.
    """
    # Create a queue of the characters.
    queue = deque('hackerrank')

    # Pop the first element of the queue when a matching character is found.
    for c in text:
        if c == queue[0]:
            queue.popleft()

            # Break early for optimization.
            if not queue:
                break

    # Contains the string if the queue is empty.
    return not queue


def main():
    """
    Solution for Algorithhms -> Strings -> Hackerrank in a String!
    """
    line_count = int(input().strip())
    lines = sys.stdin.readlines()[:line_count]
    for line in lines:
        print('YES' if contains_hackerrank(line) else 'NO')


if __name__ == '__main__':
    main()
