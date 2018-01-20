# Regex Substitution

## Problem Statement

The re.sub() (sub stands for substitution) evaluates a pattern and for each valid match, it calls a method (or lambda).
The method is called for all matches and can be used to modify strings in different ways.
The re.sub() method returns the modified string as an output.

Know more about [re.sub()](https://docs.python.org/2/library/re.html#re.sub).

Transformation of String

#### Code
```python
import re

#Squaring numbers
def square(match):
    number = int(match.group(0))
    return str(number**2)

print re.sub(r"\d+", square, "1 2 3 4 5 6 7 8 9")
```
#### Output
```
1 4 9 16 25 36 49 64 81
```
Replacements in String

#### Code
```python
import re

html = """
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">
  <!-- <param name="movie"  value="your-file.swf" /> -->
  <param name="quality" value="high"/>
</object>
"""

print re.sub("(<!--.*?-->)", "", html) #remove comment
```
#### Output
```html
<head>
<title>HTML</title>
</head>
<object type="application/x-flash"
  data="your-file.swf"
  width="0" height="0">

  <param name="quality" value="high"/>
</object>
```
## Task

You are given a text of N lines. The text contains && and || symbols.
Your task is to modify :
```
&& → and
|| → or
```
Both && and || should have space " " on both sides.

## Input Format

First line contains integer, N.
Next N lines contains the text.

## Constraints
```
0 < N < 100
```
Neither && nor || occur in start or end of each line.

## Output Format

Output the modified text.

## Sample Input
```python
11
a = 1;
b = input();

if a + b > 0 && a - b < 0:
    start()
elif a*b > 10 || a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
```
## Sample Output
```python
a = 1;
b = input();

if a + b > 0 and a - b < 0:
    start()
elif a*b > 10 or a/b < 1:
    stop()
print set(list(a)) | set(list(b))
#Note do not change &&& or ||| or & or |
#Only change those '&&' which have space on both sides.
#Only change those '|| which have space on both sides.
```
