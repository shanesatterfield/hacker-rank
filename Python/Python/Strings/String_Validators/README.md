## Problem Statement

Python has in built string validation methods for basic data validation such as checking if a string is alphabetical, alphanumeric, digit etc.

[str.isalnum()](https://docs.python.org/2/library/stdtypes.html#str.isalnum)
Check if all characters of string are alphanumeric (a-z, A-Z and 0-9).
```python
>>> print 'ab123'.isalnum()
True
>>> print 'ab123#'.isalnum()
False

```
[str.isalpha()](https://docs.python.org/2/library/stdtypes.html#str.isalpha)
Check if all characters of string are alphabetical (a-z and A-Z).
```python
>>> print 'abcD'.isalpha()
True
>>> print 'abcd1'.isalpha()
False
```

[str.isdigit()](https://docs.python.org/2/library/stdtypes.html#str.isdigit)
Check if all characters of string are digit (0-9).
```python
>>> print '1234'.isdigit()
True
>>> print '123edsd'.isdigit()
False
```

[str.islower()](https://docs.python.org/2/library/stdtypes.html#str.islower)
Check if all characters of string are lowercase characters.
```python
>>> print 'abcd123#'.islower()
True
>>> print 'Abcd123#'.islower()
False
```

[str.isupper()](https://docs.python.org/2/library/stdtypes.html#str.isupper)
Check if all characters of string are upper characters.
```python
>>> print 'ABCD123#'.isupper()
True
>>> print 'Abcd123#'.isupper()
False
```

### Task
You are given a string S.
Your task is to find if string S contains, alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

### Input Format

Single line containing, string S.

### Constraints
```
0 < len(S) < 1000
```
### Output Format

In First line, print `True` if S has alphanumeric character otherwise print `False`.
In Second line, print `True` if S has alphabetical character otherwise print `False`.
In Third line, print `True` if S has digits otherwise print `False`.
In Fourth line, print `True` if S has lowercase character otherwise print `False`.
In Fifth line, print `True` if S has uppcase character otherwise print `False`.

### Sample Input
```
qA2
```
### Sample Output
```
True
True
True
True
True
```
