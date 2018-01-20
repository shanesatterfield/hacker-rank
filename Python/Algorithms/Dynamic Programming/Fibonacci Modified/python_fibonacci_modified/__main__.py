from __future__ import print_function
import sys

def fib_mod(a, b, n):
    prev, curr, temp = a, b, b

    # Start on the second term.
    for i in range(2, n):
        curr = pow(curr, 2) + prev
        prev = temp
        temp = curr

    return curr

def main():
    input_data = [int(x) for x in sys.stdin.read().strip().split()]
    print(fib_mod(*input_data))

if __name__ == '__main__':
    main()
