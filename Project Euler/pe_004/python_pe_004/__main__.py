from __future__ import print_function
import sys, operator

palindromes = []

def pe_004(num):
    if len(palindromes) <= 0:
        find_palindromes()

    if palindromes[0] > num:
        return None

    for i in range(1, len(palindromes)):
        if palindromes[i] > num:
            return palindromes[i-1]

def find_palindromes():
    global palindromes
    start, stop = 100, 999
    palindromes = set()
    for i in range(start, stop+1):
        for j in range(start, stop+1):
            temp = i * j
            if is_palindrome(temp):
                palindromes.add(temp)

    palindromes = list(palindromes)
    palindromes.sort()

def is_palindrome(num):
    if type(num) is not str:
        num = str(num)

    if len(num) != 6:
        return False

    for i in range(len(num)):
        if num[i] != num[-(i+1)]:
            return False
    return True

def main():
    lines = [int(line) for line in sys.stdin.readlines()]
    for line in lines[1:]:
        print(pe_004(line))

if __name__ == '__main__':
    main()
