from __future__ import print_function
import sys

def greet(first_name, last_name):
    return 'Hello {} {}! You just delved into python.'.format(first_name, last_name)

def main():
    lines = [ x.strip() for x in sys.stdin.readlines()[:2] ]
    print(greet(*lines))

if __name__ == '__main__':
    main()
