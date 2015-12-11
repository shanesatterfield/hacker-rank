# Set.difference() Operation

## Problem Statement

![A-B.png.difference()](https://s3.amazonaws.com/hr-challenge-images/9420/1437904659-11e4bef847-A-B.png)
.difference() returns a set with all elements from set that are not in an iterable.
Sometimes '-' operator is used in place of .difference() operator but it operates only on the set of elements in set.
Set is immutable to .difference() operation (or '-' operation).
```python
>>> s = set("Hacker")
>>> print s.difference("Rank")
set(['c', 'r', 'e', 'H'])

>>> print s.difference(set(['R', 'a', 'n', 'k']))
set(['c', 'r', 'e', 'H'])

>>> print s.difference(['R', 'a', 'n', 'k'])
set(['c', 'r', 'e', 'H'])

>>> print s.difference(enumerate(['R', 'a', 'n', 'k']))
set(['a', 'c', 'r', 'e', 'H', 'k'])

>>> print s.difference({"Rank":1})
set(['a', 'c', 'e', 'H', 'k', 'r'])

>>> s - set("Rank")
set(['H', 'c', 'r', 'e'])
```
## Task
Students of District College have subscription of English and French newspapers. Some students have subscribed to only English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of roll numbers of students, who have subscribed to English and French newspapers. Your task is to find total number of students who have subscribed to only English newspapers.

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

Output total number of students who have only English newspaper subscriptions.

## Sample Input
```
9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
```
## Sample Output
```
4
```
## Explanation

Roll numbers of students who have only English newspaper subscription:
4, 5, 7 and 9.
Hence, total is 4 students.
