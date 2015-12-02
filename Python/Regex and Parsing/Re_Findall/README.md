# Re.findall() & Re.finditer()

## Problem Statement

[re.findall()](https://docs.python.org/2/library/re.html#re.findall)

The expression re.findall() returns all the non-overlapping matches of patterns in a string as a list of strings.

#### Code
```python
>>> import re
>>> re.findall(r'\w','http://www.hackerrank.com/')
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```
[re.finditer()](https://docs.python.org/2/library/re.html#re.finditer)

The expression re.finditer() returns an iterator yielding MatchObject instances over all non-overlapping matches for the re pattern in the string.

#### Code
```python
>>> import re
>>> re.finditer(r'\w','http://www.hackerrank.com/')
<callable-iterator object at 0x0266C790>
>>> map(lambda x: x.group(),re.finditer(r'\w','http://www.hackerrank.com/'))
['h', 't', 't', 'p', 'w', 'w', 'w', 'h', 'a', 'c', 'k', 'e', 'r', 'r', 'a', 'n', 'k', 'c', 'o', 'm']
```
## Task
You are given a string S. It consists of alphanumeric characters, spaces and symbols(+,-).
Your task is to find all the substrings of S that contains 2 or more vowels.
Also, these substrings must lie in between 2 consonants and should contain vowels only.

Note :
Vowels are defined as: `AEIOU` and `aeiou`.
Consonants are defined as: `QWRTYPSDFGHJKLZXCVBNM` and `qwrtypsdfghjklzxcvbnm`.

## Input Format

A single line of input containing string S.

## Constraints
```
0<len(S)<100
```
## Output Format

Print the matched substrings in their order of occurrence on separate lines.
If no match is found, print `-1`.

## Sample Input
```
rabcdeefgyYhFjkIoomnpOeorteeeeet
```
## Sample Output
```
ee
Ioo
Oeo
eeeee
```
## Explanation

`ee` is located between consonant d and f.
`Ioo` is located between consonant k and m.
`Oeo` is located between consonant p and r.
`eeeee` is located between consonant t and t.
