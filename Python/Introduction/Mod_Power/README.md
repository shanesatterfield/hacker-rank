# Power - Mod Power

## Problem Statement

We have only heard of the powers of Python, so far; now we will witness them :)

Power or exponent in Python can be calculated using the built-in power function. Which can be called as for a^b
```python
>>> pow(a,b)
```
or
```python
>>> a**b
```
It's also possible to calculate a^b mod m.
```python
>>> pow(a,b,m)  
```
This is very helpful in computations where you have to print result % mod.

Note that here a and b can be floats and even negatives; but if a third argument is present, b cannot be negative.

Note Python has a module math, which has its own pow() but it takes two arguments and returns a float. Frankly speaking, we will never use math.pow()

## Task
You are given three integers; print two lines.
The first line should print pow(a,b), and the second line should print the result of pow(a,b,m).

## Input Format
The first line contains a, the second line contains b, and the third line contains m.

## Constraints
```
1 ≤ a ≤ 10
1 ≤ b ≤ 10
2 ≤ m ≤ 1000
```
## Sample Input
```
3
4
5
```
## Sample Output
```
81
1
```
