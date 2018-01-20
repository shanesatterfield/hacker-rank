# Manasa Loves Math

## Problem Statement

You are given an integer N. Is there a permutation of digits of integer that's divisible by 8? A permutation of digits of integer N is defined as an integer formed by rearranging the digits of N. For example, if the number N = 123, then {123, 132, 213, 231, 312, 321} are the possible permutations.

## Input Format
The first line contains an integer T i.e. number of test cases.
T lines follow, each containing the integer N.

## Output Format
For each test case print YES if there exists one such re-arrangement of N such that it is divisible by 8 or NO if there isn't.

## Constraints
```
1 <= T <= 45
0 <= N <= 10^110
```
Note
Re-arrangements of 10 are {10, 01} which boils down to {10, 1}.

## Sample Input
```
2
61
75
```
## Sample Output
```
YES
NO
```
## Explanation
Test case \#00: 16 is permutation of 61 which is divisible by 8.  
Test case \#01: None of permutation of 75, {57, 75}, are divisible by 8.
