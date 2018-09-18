import sys


def minimum_bribes(line):
    line = list(line)
    bribes = 0
    i = len(line) - 1

    while i >= 0:
        # Difference to where the person should be in line.
        diff = line[i] - (i+1)

        # The person was too far ahead, making this impossible.
        if diff > 2:
            return None

        if diff > 0:
            # Swap entries to order the list. At most 2 at a time.
            swap_entries(line, i, diff)

            # Count the difference as a swap
            bribes += diff

        else:
            # Only move on if there was no swap.
            # If there was, it should be checked again.
            i -= 1

    return bribes


def swap_entries(arr, start, num_swaps):
    for n in range(start, start + num_swaps):
        arr[n], arr[n+1] = arr[n+1], arr[n]


def minimum_bribes_naive(line):
    bribes = 0

    for i in range(len(line)):
        curr = line[i]
        if curr > (i + 1) + 2:
            return None

        for j in line[i+1:]:
            if curr > j:
                bribes += 1

    return bribes


def main():
    lines = sys.stdin.readlines()[2::2]
    lines = (line.rstrip().split() for line in lines)
    lines = (map(int, line) for line in lines)

    for line in lines:
        bribe_count = minimum_bribes(line)
        if bribe_count is None:
            print('Too chaotic')
        else:
            print(bribe_count)


if __name__ == '__main__':
    main()
