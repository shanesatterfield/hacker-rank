from __future__ import print_function
import sys

class PE_007:
    def __init__(self, max_size=100000):
        self.primes = []
        self.collect_primes(max_size)

    def find_prime(self, index):
        if len(self.primes) == index:
            collect_primes(index*2)

        if index < 1 or index >= len(self.primes):
            return 1

        return self.primes[index-1]

    def collect_primes(self, max_primes):
        # Initialize the sieve and primes list.
        sieve = list(True for _ in range(0, max_primes))
        self.primes = []

        # Generate the sieve.
        for i in range(len(sieve)):
            for j in range(i*2+2, len(sieve), i+2):
                sieve[j] = False

        # Store results of the sieve into the primes list.
        for i in range(len(sieve)):
            if sieve[i] == True:
                self.primes.append(i+2)

def main():
    T = int(input())
    input_data = [int(x) for x in sys.stdin.readlines()[:T]]
    primer = PE_007()

    for line in input_data:
        print(primer.find_prime(line))

if __name__ == '__main__':
    main()
