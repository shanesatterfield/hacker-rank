# Re.split()

## Problem Statement

[re.split()](https://docs.python.org/2/library/re.html#re.split)

The re.split() expression splits the string by occurrence of a pattern.

## Code
```python
>>> import re
>>> re.split("-","+91-011-2711-1111")
['+91', '011', '2711', '1111']
```

## Task
You are given a string S, containing , and/or . and 0-9 digits.
Your task is to re.split() all of the , and . symbols.

## Input Format

A single line of input containing the string S.

## Output Format

Print the numbers obtained after splitting the string on separate lines.

## Sample Input
```
100,000,000.000
```
## Sample Output
```
100
000
000
000
```
Note: Each line of output should only be the numbers.
