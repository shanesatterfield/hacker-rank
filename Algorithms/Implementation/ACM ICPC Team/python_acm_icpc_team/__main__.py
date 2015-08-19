from __future__ import print_function, division
import sys, itertools
from collections import Counter

def make_teams( people ):
    # largest = bin(max([ a|b for a in people for b in people ]list(itertools.combinations(people, 2)))).count('1')
    # stuff = [ bin(a|b).count('1') for a in people for b in people ]
    # Get all different combinations of people and their combined values.
    lst = list(itertools.combinations(people, 2))

    # Turn numbers into proper, binary digit count values.
    lst = [ bin(x[0] | x[1]).count('1') for x in lst ]

    # Counts how many pairs have the largest value.
    largest = max(lst)
    return (largest, Counter(lst)[largest])

def main():
    # Read from stdin the people and the topics that they are good at.
    people = [ int(x.strip(), 2) for x in sys.stdin.readlines()[1:] ]

    # Prints out the largest number of between two people and how many teams
    # have that combined value.
    print('\n'.join(map(str, (make_teams(people)))))

if __name__ == '__main__':
    main()
