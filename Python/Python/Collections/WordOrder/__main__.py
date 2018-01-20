from __future__ import print_function
import sys, collections

def word_order(input_data):
    """Takes a series of words and returns the number of occurances in order of insertion."""
    # Count the words
    words = collections.OrderedDict()
    for word in input_data:
        if word not in words:
            words[word] = 0
        words[word] += 1

    # Return data for number of unique words and number of occurances ordered.
    return [len(words), list(words.values())]

def main():
    lines = [line.strip() for line in sys.stdin.readlines()]
    words = word_order(lines[1:])
    print( words[0])
    print(*words[1])

if __name__ == '__main__':
    main()
