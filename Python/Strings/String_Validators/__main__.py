from __future__ import print_function
import sys

def validate( string ):
    has_alpha = any( x.isalpha() for x in string )
    has_digit = any( x.isdigit() for x in string )

    return [
        has_alpha or has_digit,
        has_alpha,
        has_digit,
        any( x.islower() for x in string ),
        any( x.isupper() for x in string )
    ]

def main():
    string_input = sys.stdin.read()
    for n in validate( string_input ):
        print( n )

if __name__ == '__main__':
    main()
