from __future__ import print_function
import sys, re

def resub(text):
    return re.sub(r'(?<= )([&\|])\1(?= )', converter, text)

def converter(text):
    if text.group(0) == '&&':
        return 'and'
    elif text.group(0) == '||':
        return 'or'
    return text.group(0)

def main():
    T = int(input())
    print(resub(sys.stdin.read()))

if __name__ == '__main__':
    main()
