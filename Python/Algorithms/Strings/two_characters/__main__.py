from typing import Sequence, Set
from itertools import combinations


def reduce_to_two(text: str) -> int:
    """
    Calculate the largest string that can be found with two alternating
    character values.
    """
    letters = collect_letters(text)
    letter_pairs = combinations(letters, 2)
    largest = 0

    for pair in letter_pairs:
        delta = letters - set(pair)
        largest = calc_value(text, delta, largest)

    return largest


def calc_value(text: str, delta: Set[str], largest: int) -> int:
    """
    Calculate this instance's value and return the new largest value.
    """
    stripped = remove_letters(text, delta)
    if len(stripped) > largest and is_valid(stripped):
        return len(stripped)
    return largest


def collect_letters(text: str) -> Set[str]:
    """
    Collect a unique set of letters in the text string.
    """
    return {letter for letter in text}


def remove_letters(text: str, letters: Sequence[str]) -> str:
    """
    Remove the specified letters from the text.
    """
    return list(filter(lambda c: c not in letters, text))


def is_valid(text: str) -> bool:
    """
    Determine if the text argument is a valid solution string.
    """
    # Make sure there are exactly two unique letters.
    if len(collect_letters(text)) != 2:
        return False

    # The first two letters since this pattern repeats.
    letter_order = text[:2]

    for index, letter in enumerate(text):
        if letter != letter_order[index % 2]:
            return False
    return True


def main():
    """
    Solution for Algorithms -> Strings -> Two Characters.

    Entrypoint function that handles stdin for the script.
    """
    int(input().strip())
    s = input().strip()
    print(reduce_to_two(s))


if __name__ == '__main__':
    main()
