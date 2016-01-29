from __future__ import print_function
import sys, collections

def piling_up(arr):
    """Checks to make sure that a pile can be created from the list of numbers."""
    # Initialize the deque and start off the pile starting at infinity.
    mydq     = collections.deque(arr)
    top_pile = float('inf')

    # Iterate over the deque and check to make sure that there is always something
    # that can be added to the pile.
    while len(mydq) > 0:
        next_top = max(mydq[0], mydq[-1])
        if next_top > top_pile:
            return False

        if mydq[0] == next_top:
            top_pile = mydq.popleft()

        elif mydq[-1] == next_top:
            top_pile = mydq.pop()

    # The list of numbers was able to make a pile.
    return True



def main():
    lines = [ list(map(int, line.strip().split())) for line in sys.stdin.readlines()[2::2]]
    for line in lines:
        print("Yes" if piling_up(line) else "No")

if __name__ == '__main__':
    main()
