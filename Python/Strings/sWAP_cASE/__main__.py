from __future__ import print_function
import sys

def swap_case( text ):
    text = list(text)
    for n in range(len(text)):
        if text[n].isupper():
            text[n] = text[n].lower()
        elif text[n].islower():
            text[n] = text[n].upper()
    return ''.join(text)

def main():
    print(swap_case( sys.stdin.read() ))

if __name__ == '__main__':
    main()
