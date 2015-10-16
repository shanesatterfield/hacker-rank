from __future__ import print_function
import sys, textwrap

def text_wrap(text, width):
    return textwrap.wrap(text, int(width))

def main():
    lines = sys.stdin.readlines()[:2]
    for line in text_wrap(*lines):
        print(line)

if __name__ == '__main__':
    main()
