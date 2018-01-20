# No Idea!

## Problem Statement

There is an array of n integers, and 2 disjoint sets of m integers each A and B. You like all integers in A and dislike all integers in B. Your initial happiness is 0 and for each integer in the array, i, if i∈A, you add 1 to your happiness, if i∈B, you add −1 to your happiness, else your happiness does not change. Output your final happiness at the end.

Note that since A and B are sets, they have no repeated elements. But, the array might contain duplicate elements.

## Constraints
```
1 ≤ n ≤ 10^5
1 ≤ m ≤ 10^5
1 ≤ Any integer in the input ≤ 10^9
```
## Input Format

First line contains n and m.
Second line contains n integers, the array.
Third and fourth lines contain m integers, A and B respectively.

## Output Format

Output a single integer, the answer.

## Sample Input
```
3 2
1 5 3
3 1
5 7
```
## Sample Output
```
1
```
## Explanation

You gain 1 unit of happiness for each 3 and 1 and lose 1 unit for 5 and 7 hence total happiness is 2−1=1.
