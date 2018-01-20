from __future__ import print_function
import sys, calendar

def calmod(month, day, year):
    return calendar.day_name[calendar.weekday(year, month, day)].upper()

def main():
    print(calmod(*[int(x) for x in sys.stdin.read().strip().split()]))

if __name__ == '__main__':
    main()
