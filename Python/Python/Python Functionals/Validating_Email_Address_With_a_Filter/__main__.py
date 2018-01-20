from __future__ import print_function
import sys, re

"""
Validates a list of emails. Returns only the emails, in lexicographic order,
which are valid emails.
"""
def val_emails( emails ):
    return sorted(filter( vemail, emails ))

"""
Checks if a a string is a proper email address.
"""
def vemail( email ):
    return vemail.pattern.match(email) != None

# A static variable for the vemail validation function.
vemail.pattern = re.compile(r'^[a-zA-Z0-9\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$')

"""
Reads from stdin and runs the input through the proper functions to produce
the desired output to stdout.
"""
def main():
    T = int(input())
    lines = [ x.strip() for x in sys.stdin.readlines()[:T] ]
    print(val_emails(lines))

if __name__ == '__main__':
    main()

    # One-liner version
    # print(sorted(filter(lambda x: re.match(r'^[a-zA-Z0-9\-\_]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', x), [ x.strip() for x in sys.stdin.readlines()[1:]])))
