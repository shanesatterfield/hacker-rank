# Set .symmetric_difference() Operation

## Problem Statement

![A^B.png.symmetric_difference()](https://s3.amazonaws.com/hr-challenge-images/9421/1437912471-534f33cf60-AB.png)
.symmetric_difference() operator returns a set with all elements that are in set and iterable but not both.
Sometimes '^' operator is used in place of .symmetric_difference() operator but it operates only on the set of elements in set.
Set is immutable to .symmetricdifference() operation (or '^' operation).
```python
>>> s = set("Hacker")
>>> print s.symmetric_difference("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(set(['R', 'a', 'n', 'k']))
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(['R', 'a', 'n', 'k'])
set(['c', 'e', 'H', 'n', 'R', 'r'])

>>> print s.symmetric_difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'e', 'H', (0, 'R'), 'r', (2, 'n'), 'k', (1, 'a'), (3, 'k')])

>>> print s.symmetric_difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'Rank', 'r'])

>>> s ^ set("Rank")
set(['c', 'e', 'H', 'n', 'R', 'r'])
```
## Task
Students of District College have subscription of English and French newspapers. Some students have subscribed to only English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of roll numbers of students, who have subscribed to English and French newspapers. Your task is to find total number of students who have subscribed to English or French newspapers but not both.

## Input Format

First line contains, number of students who have subscribed to English newspaper.
Second line contains, space separated list of roll numbers of students, who have subscribed to English newspaper.
Third line contains, number of students who have subscribed to French newspaper.
Fourth line contains, space separated list of roll numbers of students, who have subscribed to French newspaper.

## Constraints
```
0<Total number of students in college<1000
```
## Output Format

Output total number of students who have subscriptions of English or French newspaper but not both.

## Sample Input
```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```
## Sample Output
```
8
```
## Explanation

Roll numbers of students who have subscriptions of English or French newspaper but not both:
4, 5, 7, 9, 10, 11, 21 and 55.
Hence, total is 8 students.
