# Validating Email Address With a Filter

## Problem Statement

You are given an integer N followed by N email addresses. Your task is to print a list containing valid email addresses, in lexicographic order.


A valid email address is of the format username@websitename.extension
Username can only contain letters, digits, dash and underscore. Website name can have letters and digits. Maximum length of the extension is 3.


## Input Format

An integer N followed by N lines containing a string

## Constraints
Each of the line is a non-empty string.

## Output Format

A list containing valid email addresses in lexicographic order. If the list is empty, just output an empty list, [].

## Sample Input
```
3
lara@hackerrank.com
brian-23@hackerrank.com
britts_54@hackerrank.com
```
## Sample Output
```python
['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']
```
## Concept
Filter takes a function returning True or False and applies it to a sequence, returning a list of only those members of the sequence for which the function returned True. A Lambda function can be used with filters.

Lets say you have to make a list of squares of integers from 0 to 9 (both included).
```python
l = list(range(10))
l = list(map(lambda x:x*x, l))
```

Now you only require those elements which are greater than 10 and less than 80.
```python
l = list(filter(lambda x: x > 10 and x < 80, l))
```
Easy isn't it!
