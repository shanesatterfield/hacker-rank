# Find a String

## Problem Statement

In this question, the user enters a string and a substring and you have to print the number of times that substring occurs in that string. String traversal will take place from left to right, not from right to left.

NOTE : Letters of string are case-sensitive.

## Input Format

Two strings each in a new line.

## Constraints

1 <= len(string) <= 200
each character in the string is an ascii character.

## Output Format

An integer number indicating the total number of occurrences of that string.

## Sample Input
```
ABCDCDC
CDC
```
## Sample Output
```
2
```
## Concept

Some string processing examples such as these might be useful.
There are a couple of new concepts :
In python, length of a string is found out by the function len(s), where s is the string.
To traverse through the length of a string, use for loop :
```python
for i in range(0, len(s)):
    print (s[i])
```
Range function is used to loop over some length, eg :
```python
range (0, 5)
```
-> loops over 0 to 4(5 excluded)
