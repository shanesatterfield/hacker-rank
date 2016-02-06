from __future__ import print_function, division
from functools import reduce
import sys, operator, math

class pe_005:
    def __init__(self, N=40):
        """Initialize the object by finding primes up to a maximum edge case."""
        self._primes = []
        self.find_primes(N)

    def find_multiple(self, num):
        """Find the smallest multiple of all numbers from 1 to the given number."""
        result = dict()
        for n in range(1, num+1):
            temp = self.find_prime_divisors(n)
            result.update({k:v for k,v in temp.items() if k not in result or result[k] < v})
        return reduce(operator.mul, (pow(k, v) for k,v in result.items()))

    def find_prime_divisors(self, num):
        """Returns a dict of the evenly divisible primes and how many times they went into the given number."""
        # If the number is prime, it is only divisible by itself.
        if pe_005.is_prime(num) or num < 2:
            return {num: 1}

        # If there were no primes searched for, then search for primes.
        if len(self._primes) <= 0:
            self.find_primes(num)

        results = dict()
        # Loop through the sorted primes list and stop when the prime is larger than the given number.
        for prime in self._primes[::-1]:
            if num <= 0:
                break

            # Count the number of divisions of the prime number into the current number.
            count, num = pe_005.count_divisions(num, prime)
            if count > 0:
                results[prime] = count

        return results

    def find_primes(self, N):
        """Find all prime numbers from 2 to the given number and store them in self._primes"""
        # If there are already primes found, start searching for primes after the last one found.
        # If the list is empty start searching at 2.
        starting_number = self._primes[-1] if len(self._primes) > 0 else 2

        # Search for primes and add them into the primes list.
        for num in range(starting_number, N+1):
            if pe_005.is_prime(num):
                self._primes.append(num)

    @staticmethod
    def count_divisions(num, n):
        """Counts the number of divisions of n into num."""
        count = 0
        while pe_005.is_divisible(num, n):
            num = num // n
            count += 1
        return count, num

    @staticmethod
    def is_divisible(num, n):
        """Checks if num is evenly divisible by n."""
        return num % n == 0

    @staticmethod
    def is_prime(num):
        """Checks if a number is prime."""
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def main():
    T = int(input())
    input_data = [int(x.strip()) for x in sys.stdin.readlines()[:T]]

    myobj = pe_005(40)
    for line in input_data:
        print(myobj.find_multiple(line))

if __name__ == '__main__':
    main()
