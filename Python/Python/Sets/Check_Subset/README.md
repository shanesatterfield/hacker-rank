# Check Subset

## Problem Statement

You are given two sets A and B.
Your job is to find whether set A is a subset of set B.

If set A is subset of set B, print True.
If set A is not a subset of set B, print False.

## Input Format

First line will contain number of testcases, T.
First line of each testcase contains number of elements in set A.
Second line of each testcase contains space separated elements of set A.
Third line of each testcase contains number of elements in set B.
Fourth line of each testcase contains space separated elements of set B.

## Constraints
```
0 < T < 21
0 < Number of elements in each set < 1001
```
## Output Format

Output True or False for each testcase in separate lines.

## Sample Input
```
3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
```
## Sample Output
```
True
False
False
```
## Explanation

## Explanation Test Case 01
```
set A = {1 2 3 5 6}
set B = {9 8 5 6 3 2 1 4 7}
```
All the elements of set A are the elements of set B.
Hence, set A is subset of set B.


`Note: More than 4 lines will result in 0 score. Blank lines won't be counted.`
