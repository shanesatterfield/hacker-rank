from __future__ import print_function, division
import sys

def minimax(p, q, arr):
    p, q      = min(p,q), max(p,q)
    arr       = sorted(arr)
    starting  = 0
    highest   = (p, 0)
    n         = min(p,q)
    max_range = q

    if q > arr[-1]:
        highest = (q, abs(arr[-1] - q))

    while n <= max_range and starting < len(arr):
        curr = float('inf')

        for i in range(starting, len(arr)):
            temp = abs(arr[i] - n)

            # Break if you found something less than current best. No need in continuing.
            if temp <= highest[1]:
                curr = temp
                starting = i
                break

            # Break if you found something larger than the min. The list is sorted,
            # so all elements after will be larger.
            elif temp >= curr:
                break

            # Set the current min for this number and increase the starting position.
            # No need to start earlier. You would only find values that are
            # larger than the previous one.
            else:
                curr     = temp
                starting = i

        # If you found a higher minimax, update.
        if curr > highest[1] and curr < float('inf'):
            highest = (n, curr)

        n = max(n+1, arr[starting] + highest[1] + 1)

    return highest[0]

def main():
    lines = [[int(b) for b in x.strip().split()] for x in sys.stdin.readlines()]
    print(minimax(lines[2][0], lines[2][1], lines[1]))

if __name__ == '__main__':
    main()
