import sys


def main():
    arr = sys.stdin.readlines()[1].strip().split()
    arr = tuple(int(x) for x in arr)
    result = max_array_sum(arr)
    print(result)


def max_array_sum(arr=[]):
    largest = float('-inf')
    prev = largest
    prev_2 = largest

    for n in reversed(range(len(arr))):
        curr = arr[n]
        curr = max(curr, prev, prev_2, curr + prev_2)

        prev_2 = prev
        prev = curr

        if curr > largest:
            largest = curr

    return largest


def max_array_sum_recursive(arr=[], total=0):
    if len(arr) == 0:
        return total
    if len(arr) == 1:
        return max(total, total + arr[0])

    largest = total
    for n in reversed(range(len(arr))):
        curr = max_array_sum_recursive(arr[n+2:], total + arr[n])
        if curr > largest:
            largest = curr
    return largest


if __name__ == '__main__':
    main()
