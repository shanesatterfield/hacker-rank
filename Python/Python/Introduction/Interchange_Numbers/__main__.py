from __future__ import print_function

def interchange(a, b):
    return (b, a)

def main():
    a, b = int(input()), int(input())
    for line in interchange(a, b):
        print(line)

if __name__ == '__main__':
    main()
