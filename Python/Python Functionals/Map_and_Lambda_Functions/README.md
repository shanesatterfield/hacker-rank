# Map and Lambda Functions

## Problem Statement

Let's learn some new python concepts! You have to generate a list of the first N fibonacci numbers, 0 being the first number. Then, apply the map function and a lambda expression to cube each fibonacci number and print the list.

## Input Format

An integer N

## Output Format

A list containing cubes of first N fibonacci numbers.

## Constraints
0<=N<=15

## Sample Input
```python
5
```
## Sample Output
```python
[0, 1, 1, 8, 27]
```
The first 5 fibonacci numbers are [0, 1, 1, 2, 3] and their cubes are [0, 1, 1, 8, 27]

## Concept

The map() function applies a function to every member of an iterable and returns the result. It takes two parameters, first the function which is to be applied and second the iterables like a list.
Let's say you are given a list of names and you have to print a list which contains length of each name.
```python
>> print (list(map(len, ['Tina', 'Raj', 'Tom'])))  
[4, 3, 3]  
```
Lambda is a single expression anonymous function often used as an inline function. In simple words, it is a function which has only one line in its body. It proves very handy in functional and GUI programming.
```python
>> sum = lambda a, b, c: a + b + c
>> sum(1, 2, 3)
6
```
Note:

Lambda functions cannot use the return statement and can only have a single expression. Unlike def, which creates a function and assigns it a name, lambda creates a function and returns the function itself. Lambda can be used inside list and dictionary.
