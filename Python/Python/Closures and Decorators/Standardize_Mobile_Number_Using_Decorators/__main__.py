from __future__ import print_function
import sys, re

class formatter:
    """Decorator for formatting mobile phone numbers."""
    # Regex pattern to collect phone number data.
    pattern = re.compile(r'^(\+91|91|0){0,1}(\d{10})$')

    def __init__(self, func):
        """Constructor that takes a function."""
        self.func = func

    @staticmethod
    def formatNum(num):
        """Static method for formatting a mobile phone number."""
        num_str = formatter.pattern.match(num).group(2)
        return '+91 ' + num_str[0:5] + ' ' + num_str[5:10]

    def __call__(self, arr):
        """Decorator method for calling the decorated function and passing it the formatted numbers."""
        arr = list(map(formatter.formatNum, arr))
        return self.func(arr)

@formatter
def stand(arr):
    """Decorated function that sorts a list of mobile phone numbers."""
    return sorted(arr)

def main():
    T = int(input())
    lines = [line.strip() for line in sys.stdin.readlines()[:T]]
    for number in stand(lines):
        print(number)

if __name__ == '__main__':
    main()
