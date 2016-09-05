from __future__ import print_function

def weird(n):
    if n % 2 == 0 and (n >= 2 and n <= 5 or n > 20):
        return 'Not Weird'
    return 'Weird'

def main():
    print(weird(int(input())))

if __name__ == '__main__':
    main()
