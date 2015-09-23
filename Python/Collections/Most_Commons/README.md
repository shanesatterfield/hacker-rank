# Most Commons

## Problem Statement

You are given a string S.
The string consists of lowercase alphabets.

Your task is to find top three most common characters in the string S.

## Input Format

Single line containing string S.

## Constraints
```
3 < len(S) < 104
```
## Output Format

Print the most common characters along with their count of occurrences in three lines.
Output must sorted in descending order of count of occurrences.
If count of occurrences is same then sort in ascending order of characters.

## Sample Input
```
aabbbccde
```
## Sample Output
```
b 3
a 2
c 2
```
## Explanation

b is occurring 3 times. Hence, it is printed first.
Both a and c occur 2 times. So, a is printed in second line and c in third line because in ascending order of alphabets a comes ahead of c.

Note: The string S has at least 3 distinct characters.
