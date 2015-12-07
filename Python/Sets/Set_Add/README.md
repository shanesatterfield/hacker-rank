# Set.add()

## Problem Statement

If we want to add a single element to an existing set, then we can use .add() operation.
It adds element to the set and returns 'None'.

## Example
```python
>>> s = set('HackerRank')
>>> s.add('H')
>>> print s
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
>>> print s.add('HackerRank')
None
>>> print s
set(['a', 'c', 'e', 'HackerRank', 'H', 'k', 'n', 'r', 'R'])
```
## Task

Apply your knowledge of .add() operation, to help your friend 'Hari'.

Hari has a huge collection of country stamps. He decided to count total number of distinct country stamps he has collected. He asked you to help him. You pick stamps one by one from a stack of 'N' country stamps.

Your task is to find the total number of distinct country stamps.

## Input Format

First line contains N, total number of country stamps.
Next N lines contains, names of the country stamp.
## Constraints
```
0 < N < 1000
```
## Output Format

Output the total number of distinct country stamps.

## Sample Input
```
7
UK
China
USA
France
New Zealand
UK
France
```
Sample Output
```
5
```
## Explanation

UK and France are repeating twice. Hence, total number of distinct country stamps is 5 (five).
