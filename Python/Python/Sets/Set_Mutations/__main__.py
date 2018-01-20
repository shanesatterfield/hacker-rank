from __future__ import print_function
import sys

# Dictionary of possible commands.
commands = {
    "intersection_update":         set.intersection_update,
    "update":                      set.update,
    "symmetric_difference_update": set.symmetric_difference_update,
    "difference_update":           set.difference_update
}

# Runs a command on two given sets.
def mutate(command, a, b):
    commands[command](a, b)
    return a

def main():
    lines = [line.strip().split() for line in sys.stdin.readlines()[1:]]

    # The original set.
    orig  = set(map(int, lines[0]))

    # Run the mutation commands on the original set.
    for command in pair_up(lines[2:], 2):
        mutate(command[0][0], orig, map(int, command[1]))

    print(sum(orig))

# Takes an iterable and returns a list of the elements grouped up of size n.
def pair_up(arr, n):
    for i in range(0, len(arr), n):
        yield arr[i:i+n]

if __name__ == '__main__':
    main()
