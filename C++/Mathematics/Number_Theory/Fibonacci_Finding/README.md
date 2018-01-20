# Fibonacci Finding

## Problem Statement

You're given three numbers: A, B, and N, and all you have to do is to find the number FN where
```
F0=A
F1=B
Fi=Fi−1+Fi−2 for i≥2
```
As the number can be very large, output it modulo 109+7.

Consider the following link: [http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form](http://en.wikipedia.org/wiki/Fibonacci_number#Matrix_form)

## Input Format
First line contains a single integer T - the number of tests. T lines follow, each containing three integers: A, B and N.

Constraints
```
1 ≤ T ≤ 1000
1 ≤ A,B,N ≤ 109
```
## Output Format
For each test case output a single integer − FN.

## Sample Input
```
8  
2 3 1  
9 1 7  
9 8 3  
2 4 9  
1 7 2  
1 8 1  
4 3 1  
3 7 5  
```
## Sample Output
```
3  
85  
25  
178  
8  
8  
3  
44
```
## Explanation
First test case is obvious.
Let's look through the second one:
```
F0=9
F1=1
F2=1+9=10
F3=10+1=11
F4=11+10=21
F5=21+11=32
F6=32+21=53
F7=53+32=85
```
