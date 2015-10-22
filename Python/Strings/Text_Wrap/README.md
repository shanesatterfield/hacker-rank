# Text Wrap

## Problem Statement

## Textwrap

The textwrap module provides two convenience functions, wrap() and fill().

## textwrap.wrap()

Wraps the single paragraph in text (a string) so every line is at most width characters long.
Returns a list of output lines.
```python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.wrap(string,8)
['This is', 'a very', 'very', 'very', 'very', 'very', 'long', 'string.']
```

## textwrap.fill()

Wraps the single paragraph in text, and returns a single string containing the wrapped paragraph.
```python
>>> import textwrap
>>> string = "This is a very very very very very long string."
>>> print textwrap.fill(string,8)
This is
a very
very
very
very
very
long
string.
```
## Task

You are given string S and width w.
Your task is to wrap the string into a paragraph of width w.

## Input Format

First line contains, string S.
Second line contains, width w.

## Constraints
```
0 < len(S) < 1000
0 < w < len(S)
```
## Output Format

Print the text wrapped paragraph.

## Sample Input
```
ABCDEFGHIJKLIMNOQRSTUVWXYZ
4
```
## Sample Output
```
ABCD
EFGH
IJKL
IMNO
QRST
UVWX
YZ  
```
