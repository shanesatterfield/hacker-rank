from __future__ import print_function, division, generators
import sys

def mutate( string, index, new_char ):
    index = int(index)
    return string[:index] + new_char + string[index+1:]

def main():
    lines = sys.stdin.readlines()[:2]

    string = lines[0]
    args = lines[1].split()

    print(mutate(string, int(args[0]), args[1]))

if __name__ == '__main__':
    main()
