# Text Alignment

## Problem Statement

In python, a string of text can be aligned left, right and center.

.ljust(width)

Returns left aligned string of length width.
```python
>>> width = 20
>>> print 'HackerRank'.ljust(width,'-')
HackerRank----------  
.center(width)
```
Returns centered string of length width.
```python
>>> width = 20
>>> print 'HackerRank'.center(width,'-')
-----HackerRank-----
.rjust(width)
```
Returns right aligned string of length width.
```python
>>> width = 20
>>> print 'HackerRank'.rjust(width,'-')
----------HackerRank
```
## Task

You are given a partial code, used for generating HackerRank Logo of variable thickness.
Your task is to replace the blank (______) with rjust, ljust or center.

## Input Format

Single line containing, the thickness value of logo.

## Constraints

Thinkness must be an odd number.
```
0 < thickness < 50
```
## Output Format

Output the desired logo.

## Sample Input
```
5
```
## Sample Output
```
    H
   HHH
  HHHHH  
 HHHHHHH
HHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHHHHHHHHHHHHHHHHHHHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
  HHHHH               HHHHH
                    HHHHHHHHH
                     HHHHHHH  
                      HHHHH
                       HHH
                        H
```
