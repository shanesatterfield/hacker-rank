from __future__ import print_function
import sys

def design(R, C):
    lines = list()

    for n in range(1, R//2 + 1):
        line = ('.|.' * (n*2-1)).center(C, '-')
        lines.append(line)

    lines.append('WELCOME'.center(C, '-'))
    lines.extend(reversed(lines[:-1]))
    return lines

def main():
    N, M = [ int(x) for x in sys.stdin.read().strip().split()[:2] ]
    for line in design(N, M):
        print(line)

if __name__ == '__main__':
    main()


# Only accepts 6 lines of code or less.
#
# R, C = [ int(x) for x in sys.stdin.read().strip().split()[:2] ]
# lines = [ ('.|.' * (n*2-1)).center(C, '-') for n in range(1, R//2 + 1) ]
# lines += ['WELCOME'.center(C, '-')] + list(reversed(lines))
# print('\n'.join(lines))
