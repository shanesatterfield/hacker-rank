# Integer Come In All Sizes

## Problem Statement

Integers in Python can be as big as the bytes in your machine's memory. There is no limit of 2^31−1 (c++ int) or 2^63−1 (C++ long long int). Let's try this out.

As we know, the result of a^b grows really fast with increasing b.

We will do some calculations on very large integers.

## Task
Read four numbers, a, b, c, and d, and print the result of a^b+c^d.

Input Format
Four numbers are given on four lines.

## Constraints
```
1 ≤ a ≤ 1000
1 ≤ b ≤ 1000
1 ≤ c ≤ 1000
1 ≤ d ≤ 1000
```
Output Format
Print the result in one line.

## Sample Input
```
9
29
7
27
```
## Sample Output
```
4710194409608608369201743232  
```
Note that this result is bigger than 2^63−1 and hence won't fit in long long int of C++ or a 64-bit integer.
