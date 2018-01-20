# Set.intersection() Operation

## Problem Statement

![A&B.png.intersection()](https://s3.amazonaws.com/hr-challenge-images/9419/1437830945-a56a63892c-AB.png)
.intersection() operator returns the intersection of set and the set of elements in an iterable.
Sometimes '&' operator is used in place of .intersection() operator but it operates only on the set of elements in set.
Set is immutable to .intersection() operation (or '&' operation).
```python
>>> s = set("Hacker")
>>> print s.intersection("Rank")
set(['a', 'k'])

>>> print s.intersection(set(['R', 'a', 'n', 'k']))
set(['a', 'k'])

>>> print s.intersection(['R', 'a', 'n', 'k'])
set(['a', 'k'])

>>> print s.intersection(enumerate(['R', 'a', 'n', 'k']))
set([])

>>> print s.intersection({"Rank":1})
set([])

>>> s & set("Rank")
set(['a', 'k'])
```
## Task
Students of District College have subscription of English and French newspapers. Some students have subscribed to only English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of roll numbers of students, who have subscribed to English and French newspapers. Your task is to find total number of students who have subscribed to both newspapers.

## Input Format

First line contains, number of students who have subscribed to English newspaper.
Second line contains, space separated list of roll numbers of students, who have subscribed to English newspaper.
Third line contains, number of students who have subscribed to French newspaper.
Fourth line contains, space separated list of roll numbers of students, who have subscribed to French newspaper.

## Constraints
```
0 < Total number of students in college < 1000
```
## Output Format

Output total number of students who have subscriptions in both English and French.

## Sample Input
```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```
## Sample Output
```
5
```
## Explanation

Roll numbers of students who have both subscriptions:
1, 2, 3, 6 and 8.
Hence, total is 5 students.
