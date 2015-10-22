# itertools.combinations()

## Problem Statement

[itertools.combinations(iterable, r)](https://docs.python.org/2/library/itertools.html#itertools.combinations)
Return r length subsequences of elements from the input iterable.

Combinations are emitted in lexicographic sort order. So, if the input iterable is sorted, the combination tuples will be produced in sorted order.

## Sample Code
```python
>>> from itertools import combinations
>>>
>>> print list(combinations('12345',2))
[('1', '2'), ('1', '3'), ('1', '4'), ('1', '5'), ('2', '3'), ('2', '4'), ('2', '5'), ('3', '4'), ('3', '5'), ('4', '5')]
>>>
>>> A = [1,1,3,3,3]
>>> print list(combinations(A,4))
[(1, 1, 3, 3), (1, 1, 3, 3), (1, 1, 3, 3), (1, 3, 3, 3), (1, 3, 3, 3)]
```
## Task

You are given a string S.
Your task is to print all possible combinations up to size k, of the string in lexicographic sorted order.

## Input Format

Single line containing space separated , string S and value k.

## Constraints
```
0 < k ≤ len(S)
```
String contains only UPPERCASE characters.

## Output Format

Print combinations of string S in separate lines.

## Sample Input
```
HACK 2
```
## Sample Output
```
A
C
H
K
AC
AH
AK
CH
CK
HK
```
