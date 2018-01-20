# Mutations

## Problem Statement

We have seen that lists are mutable (you can make changes) and tuples on the other hand are immutable (you can't make changes).

Let's try to understand this with an example.

You are given a string(immutable) and you want to make changes in it.

Example
```
>>> string = "abracadabra"
```
You can access an index as
```
>>> print string[5]
a
```
What if you would like to assign a value?
```
>>> string[5] = 'k'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'str' object does not support item assignment
```
How would you approach this?

One solution is to convert the string to a list and then change the value.

Example
```
>>> string = "abracadabra"
>>> l = list(string)
>>> l[5] = 'k'
>>> string = ''.join(l)
>>> print string
abrackdabra
```
Another approach is to slice the string and join it back.
```
Example

>>> string = string[:5] + "k" + string[6:]
>>> print string
abrackdabra
```
## Task
You have to read a string. change the character at a given index and print the string.

## Input Format
First line contains a string, S.
Next line contains an integer i and a character c.

## Output Format
Using any of the method explained above. Replace the character at index i with c.

## Sample Input
```
abracadabra
5 k
```
## Sample Output
```
abrackdabra
```
