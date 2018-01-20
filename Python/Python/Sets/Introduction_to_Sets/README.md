# Introduction to Sets

## Problem Statement

A set is an unordered collection without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.

## Example
```python
>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
```
Basically, sets are used for membership testing and eliminating duplicate entries.

## Task

Now, lets use our knowledge of Sets and help 'Mickey'.

Ms. Gabriel Williams is a botany professor at District College. One day, she asked her student 'Mickey' to compute an average of all the plants with distinct heights in her greenhouse.

Formula used:
Average=SumofDistinctHeights / TotalNumberofDistinctHeights
## Input Format

First line contains, total number of plants in greenhouse.
Second line contains, space separated height of plants in the greenhouse.
Total number of plants is upto 100 plants.

## Output Format

Output the average value of height.

## Sample Input
```
10
161 182 161 154 176 170 167 171 170 174
```
## Sample Output
```
169.375
```
## Explanation

`set([154, 161, 167, 170, 171, 174, 176, 182])`, is the set containing distinct heights. Using `sum()` and `len()` functions we can compute the average.

`Average=1355 / 8=169.375`
