import sys


def count_camel_words(text: str) -> int:
    """
    Takes a camel case string and returns how many words are in the string.
    """
    has_starting_word = 1 if len(text) > 0 else 0
    return len(list(filter(lambda x: x.isupper(), text))) + has_starting_word


def main():
    """
    Solution for Algorithms -> Strings -> Camel Case

    Alice wrote a sequence of words in CamelCase as a string of letters, s,
    having the following properties:

    It is a concatenation of one or more words consisting of English letters.

    All letters in the first word are lowercase.

    For each of the subsequent words, the first letter is uppercase and rest of
    the letters are lowercase.

    Given s, print the number of words in s on a new line.
    """
    print(count_camel_words(sys.stdin.read().strip()))


if __name__ == '__main__':
    main()
