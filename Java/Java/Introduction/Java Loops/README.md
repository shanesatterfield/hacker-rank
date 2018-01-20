# Java Loops

## Problem Statement

In this problem you will test your knowledge of Java loops. Given three integers a, b, and n, output the following series:

    a+2^0b,a+2^0b+2^1b,......,a+2^0b+2^1b+...+2^n−1b

## Input Format

The first line will contain the number of integers, t. Each of the next t lines will have three integers, a, b, and n.

*Constraints*:
```
0 ≤ a,b ≤ 50
1 ≤ n ≤ 15
```
## Output Format

Print the answer to each test case in seperate lines.

## Sample Input
```
2
0 2 10
5 3 5
```
## Sample Output
```
2 6 14 30 62 126 254 510 1022 2046
8 14 26 50 98
```
## Explanation

In the first case:
```
1st term=0+1*2=2
2nd term=0+1*2+2*2=6
3rd term=0+1*2+2*2+4*2=14
```
and so on.
