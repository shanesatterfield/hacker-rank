from __future__ import print_function
import sys

def time_convert(time_string):
    pm = time_string[-2:] == 'PM'
    time_string = time_string[:-2].split(':')
    hour = int(time_string[0])

    hour = hour % 12
    if pm:
        hour += 12

    time_string[0] = '{0:02d}'.format(hour)
    return ':'.join(time_string)

def main():
    print(time_convert(sys.stdin.read().strip()))

if __name__ == '__main__':
    main()
