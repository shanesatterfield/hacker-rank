from __future__ import print_function
import sys, re

def refindall(text):
    result = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])[AIEOUaeiou]{2,}(?=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])', text)
    return result if len(result) > 0 else ['-1']

def main():
    for line in refindall(sys.stdin.read()):
        print(line)

if __name__ == '__main__':
    main()
