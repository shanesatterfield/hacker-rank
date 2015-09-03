from __future__ import print_function, division
import sys

def fizzbuzz(start, stop):
    line = None
    lst = []
    for n in range(start, stop+1):
        line = ''
        if n % 3 == 0:
            line += 'Fizz'
        if n % 5 == 0:
            line += 'Buzz'

        lst.append(line or n)

    return lst

def main():
    for n in fizzbuzz(1, 100):
        print(n)

if __name__ == '__main__':
    main()

# Short Version
#print('\n'.join(['FizzBuzz'if x%15==0 else'Fizz' if x%3==0 else'Buzz' if x%5==0 else str(x) for x in range(1,101)]))

# Other Short Version
"""
for n in range(start, stop+1):
    line = ''
    if n % 3 == 0:
        line += 'Fizz'
    if n % 5 == 0:
        line += 'Buzz'
    print(line or n)
"""
