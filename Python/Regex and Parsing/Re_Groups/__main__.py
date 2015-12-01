from __future__ import print_function
import sys, re

def regroups(text):
    result = re.search(r'([0-9A-Za-z])\1{1,}', text)
    return result.group(1) if result else '-1'

def main():
    print(regroups(sys.stdin.read()))

if __name__ == '__main__':
    main()
