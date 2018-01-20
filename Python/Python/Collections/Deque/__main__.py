from __future__ import print_function
import sys, collections

deq_commands = {
    'append':     collections.deque.append,
    'pop':        collections.deque.pop,
    'appendleft': collections.deque.appendleft,
    'popleft':    collections.deque.popleft
}

def deq(commands):
    """Returns the results of a list of commands run on a new deque instance."""
    # Creates the deque.
    mydeque = collections.deque()

    # Runs the commands on the deque instance.
    for comm in commands:
        deq_commands[comm[0]](mydeque, *comm[1])

    return mydeque


def main():
    # Parses the input. The first element is the command string.
    # The second element is a list that containts the possible arguemnts for the function.
    lines = [[x[0], list(map(int, x[1:]))] for x in [line.strip().split() for line in sys.stdin.readlines()]][1:]

    # Print the output to stdout.
    print(*deq(lines))

if __name__ == '__main__':
    main()
