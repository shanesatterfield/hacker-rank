# Find second largest number in a list

## Problem Statement

Now, lets delve into one of the most basic data types in python, LIST. You are given 'n' numbers. Store them in a list and find the second largest number. Easy enough!

NOTE : Don't use insertion sort

## Input Format

First line contains N. Second line contains Array A[] of N integers each separated by a space.

## Output Format

Value of the second largest number.

## Sample Input
```
5
2 3 6 6 5
```
## Sample Output
```
5
```
## Constraints
```
2 <= N <= 10
-100 <= A[i] <= 100
```
## Concept

A list in python is similar to an array. A list can contain any datatype, even mixed datatype i.e. a list can contain a number, a string and even another list.
List is mutable, i.e. values can be added and removed from the list.

Eg :
```python
>> a = [] # Define an empty
>> a.append(5) # Add a new element to a list
>> a.append(3)
>> a.append(7)
>> len(a) # Find length of the list
3
>> a[0]*a[2] # Indexing of list starts from 0
35
>> a.pop() # Removes the last element of the list and returns its value
7
>> a.remove(5) # Removes the first occurence of the element from the list.
>> a
[3]
>> a.extend([3,2]) # Appends a list at the end of another list
>> a
[3, 3, 2]
```
