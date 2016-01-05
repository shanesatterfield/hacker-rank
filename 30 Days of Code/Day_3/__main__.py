from __future__ import print_function

def day3(num):
    return 'Not Weird' if num % 2 == 0 and (num < 6 or num > 20) else 'Weird'
    
def main():
    print(day3(int(input())))

if __name__ == '__main__':
    main()
