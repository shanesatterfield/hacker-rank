from typing import List, Tuple
import sys


def main():
    lines = sys.stdin.readlines()[1]
    scores = [int(x) for x in lines.split()]
    print(*get_record_breaks(scores))


def get_record_breaks(scores: List[int]) -> Tuple[int, int]:
    """
    Get the number of times the max record has increased and the min record
    has decreased.
    """
    if not scores or len(scores) <= 1:
        return 0, 0

    max_score = scores[0]
    min_score = scores[0]
    max_break = 0
    min_break = 0

    for score in scores:
        if score > max_score:
            max_score = score
            max_break += 1

        elif score < min_score:
            min_score = score
            min_break += 1

    return max_break, min_break


if __name__ == '__main__':
    main()
