# Interchange Two Numbers

## Problem Statement

You are given two integers. Store them into two variables and exchange them. Can it get any easier! Make sure to use a tuple to do the task, rather than using any fancy logic. Print the two numbers.

## Input Format

Two integers

## Output Format

Two integers

## Sample Input
```
2
1
```
## Sample Output
```
1
2
```
## Concept

A tuple is similar to a list. The difference is that a tuple is immutable i.e. it cannot be changed. Once you assign some value to a tuple, it cannot be changed. Also, no additional members can be added once a tuple is assigned.

Eg:
```python
>> a = 1, # Define a tuple with one member
>> a = (2, 6)
>> a[1] = 1 # Can't alter the elements in tuple
TypeError: 'tuple' object does not support item assignment
```
For traversing a tuple, the method is similar to that of a list. Tuples are most commonly used to assign more than one variables in one statement i.e. for simultaneous assignment.
