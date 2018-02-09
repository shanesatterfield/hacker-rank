import sys
from enum import Enum


class Acid(Enum):
    NON_METAL = 'non-metal acid'
    POLYATOMIC = 'polyatomic acid'
    NOT_ACID = 'not an acid'


def name_acid(text: str) -> Acid:
    hydro = text.startswith('hydro')
    poly = text.endswith('ic')

    if hydro and poly:
        return Acid.NON_METAL
    elif poly:
        return Acid.POLYATOMIC
    return Acid.NOT_ACID


def main():
    lines = [line.strip() for line in sys.stdin.readlines()][1:]
    for line in lines:
        print(name_acid(line).value)


if __name__ == '__main__':
    main()
