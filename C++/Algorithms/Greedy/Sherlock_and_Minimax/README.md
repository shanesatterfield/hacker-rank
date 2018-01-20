# Sherlock and Minimax

## Problem Statement

[Русский](https://hr-filepicker.s3.amazonaws.com/101may14/russian/2491-sherlock-and-minimax.pdf) | [中文](https://hr-filepicker.s3.amazonaws.com/101may14/chinese/2491-sherlock-and-minimax.pdf)
Watson gives Sherlock an array A1,A2...AN.
He asks him to find an integer M between P and Q(both inclusive), such that, min {|Ai-M|, 1 ≤ i ≤ N} is maximised. If there are multiple solutions, print the smallest one.

## Input Format
The first line contains N. The next line contains space separated N integers, and denote the array A. The third line contains two space separated integers denoting P and Q.

## Output Format
In one line, print the required answer.

## Constraints
```
1 ≤ N ≤ 102
1 ≤ Ai ≤ 109
1 ≤ P ≤ Q ≤ 109
```
## Sample Input
```
3
5 8 14
4 9
```
## Sample Output
```
4
```
## Explanation
For M = 4,6,7, or 9, the result is 1. Since we have to output the smallest of the multiple solutions, we print 4.
