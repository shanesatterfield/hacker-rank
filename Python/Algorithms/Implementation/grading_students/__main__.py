import sys


def grade_student(grade: int) -> int:
    if grade < 38:
        return grade

    next_mult = ((grade // 5) + 1) * 5

    if next_mult - grade < 3:
        return min(next_mult, 100)

    return grade


def main():
    """
    Solution for Algorithms -> Implementation -> Grading Students.
    """
    num_cases = int(input().strip())
    lines = [int(x.strip()) for x in sys.stdin.readlines()][:num_cases]
    for line in lines:
        print(grade_student(line))


if __name__ == '__main__':
    main()
