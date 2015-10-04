from __future__ import print_function
import sys

def factorial(N):
    result = 1
    for n in range(1, N+1):
        result *= n
    return result

def main():
    print(factorial(int(input())))

if __name__ == '__main__':
    main()
