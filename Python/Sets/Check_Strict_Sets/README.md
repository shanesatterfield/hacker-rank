# Check Strict Sets

## Problem Statement

You are given a set A and N numbers of other sets.
Your job is to find whether set A is a strict superset of all the N sets.
Print True, if it is a strict superset of all N sets otherwise print False.

A strict superset has atleast one element which not in its subset.

Example:  
`set([1, 3, 4])` is a strict superset of `set([1,3])`.  
`set([1, 3, 4])` is not a strict superset of `set([1, 3, 4])`.  
`set([1, 3, 4])` is not a strict superset of `set([1, 3, 5])`.  

## Input Format

First line contains, space separated elements of set A.
Second line contains, integer N.
Next N lines contain, space separated elements of other sets.

## Constraints
```
0<len(set(A))<501
0<N<21
0<len(otherSets)<101
```
## Output Format

Print True if set A is strict superset of all N the sets otherwise print False.

## Sample Input
```
1 2 3 4 5 6 7 8 9 10 11 12 23 45 84 78
2
1 2 3 4 5
100 11 12
```
## Sample Output
```
False
```
## Explanation

Set A is the strict superset of set([1, 2, 3, 4, 5]) but not set([100, 11, 12]) because 100 is not in set A.
Hence, the output is False.
