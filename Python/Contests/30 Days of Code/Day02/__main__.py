from __future__ import print_function, division
import sys, math

def day_2(M, T, X):
    result = int(round((M + (M*T/100) + (M*X/100))))
    print("The final price of the meal is ${}.".format(result))

def main():
    lines = [float(line) for line in sys.stdin.readlines()[:3]]
    day_2(*lines)

if __name__ == '__main__':
    main()
