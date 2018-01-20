# Mod Divmod

## Problem Statement

One of the built-in functions of Python is divmod, which takes two arguments a and b and returns a tuple containing the quotient of a/b (a//b) and remainder a.

Here a/b can be compared with integer division a//b.
```python
>>> print divmod(177,10)
(17, 7)
```
Here 177/10 => 17 and 177%10 => 7

## Task
Read two integers, a and b, and print three lines.
The first line is the integer division a//b (Remember to import division from __future__)
The second line is the result of a%b. (Modulo operator)
In the third line print the divmod of a and b.

## Input Format
The first line contains the first integer, a, and the second line contains the second integer, b.

## Output Format
Print the result as described above.

## Sample Input
```
177
10
```
## Sample Output
```
17
7
(17, 7)
```
