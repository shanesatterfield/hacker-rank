import sys


def kangaroo(x1: int, v1: int, x2: int, v2: int) -> bool:
    """
    Do some algebra; solve for x.

    if x1, v1 are 0, 3 and x2, v2 are 4, 2, then solve for x in the given
    equation.

    3x = 2x + 4

    If x is negative, then they never meet. If x is positive, then that's the
    number of sets to take before they meet.

    Also make sure that they are whole steps.
    """
    v = v1 - v2
    x = x2 - x1

    if v < 0:
        v *= -1
        x *= -1

    return x >= 0 and v != 0 and x % v == 0


def main():
    """
    Solution for Algorithms -> Implementation -> Kangaroo.
    """
    args = [int(x) for x in sys.stdin.read().strip().split()]
    print('YES' if kangaroo(*args) else 'NO')


if __name__ == '__main__':
    main()
