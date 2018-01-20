from __future__ import print_function

def num_lines(num):
    lines = list()
    width = len(bin(num)) - 2

    for n in range(1, num+1):
        line = '{1: >{0}d} {1: >{0}o} {1: >{0}X} {1: >{0}b}'.format(width, n)
        lines.append(line)

    return lines

def main():
    T = int(input())
    for line in num_lines(T):
        print(line)

if __name__ == '__main__':
    main()
