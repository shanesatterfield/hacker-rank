from __future__ import print_function, division
import sys

def caesar( string, k ):
    new_string = []
    for n in string:
        letter = ord(n)
        if n.isalpha():
            capital = int(n.isupper())
            # Drop value to start at zero.
            letter -= caesar.ascii_diff[capital]

            # Add in the cypher properly to determine letter.
            letter = (letter + k) % 26

            # Add back the base ascii value so that it knows if it was capital or not.
            letter += caesar.ascii_diff[capital]

        new_string.append(chr(letter))

    return ''.join(new_string)

caesar.ascii_diff = [97, 65]

def main():
    lines = [ x.strip() for x in sys.stdin.readlines()[1:3] ]
    print(caesar(lines[0], int(lines[1])))

    # One-liner
    # print(''.join([ chr((ord(n) - (65 if n.isupper() else 97) + int(lines[1])) % 26 + (65 if n.isupper() else 97)) if n.isalpha() else n for n in lines[0] ]))
if __name__ == '__main__':
    main()
