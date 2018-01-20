# itertools.permutations()

## Problem Statement

[itertools.permutations(iterable[, r])](https://docs.python.org/2/library/itertools.html#itertools.permutations)

Returns successive r length permutations of elements in an iterable.

If r is not specified or is None, then r defaults to the length of the iterable and all possible full-length permutations are generated.

Permutations are emitted in lexicographic sort order. So, if the input iterable is sorted, the permutation tuples will be produced in sorted order.

## Sample Code
```python
>>> from itertools import permutations
>>> print permutations(['1','2','3'])
<itertools.permutations object at 0x02A45210>
>>>
>>> print list(permutations(['1','2','3']))
[('1', '2', '3'), ('1', '3', '2'), ('2', '1', '3'), ('2', '3', '1'), ('3', '1', '2'), ('3', '2', '1')]
>>>
>>> print list(permutations(['1','2','3'],2))
[('1', '2'), ('1', '3'), ('2', '1'), ('2', '3'), ('3', '1'), ('3', '2')]
>>>
>>> print list(permutations('abc',3))
[('a', 'b', 'c'), ('a', 'c', 'b'), ('b', 'a', 'c'), ('b', 'c', 'a'), ('c', 'a', 'b'), ('c', 'b', 'a')]
```
## Task

You are given a string S.
Your task is to print all possible permutations of size k of the string in lexicographic sorted order.

## Input Format

Single line containing space separated , string S and value k.

## Constraints
```
0 < k ≤ len(S)
```
String contains only UPPERCASE characters.

## Output Format

Print permutations of string S in separate lines.

## Sample Input
```
HACK 2
```
## Sample Output
```
AC
AH
AK
CA
CH
CK
HA
HC
HK
KA
KC
KH
```
## Explanation

All possible permutations of size 2 of this string "HACK" are printed in lexicographic sorted order.
