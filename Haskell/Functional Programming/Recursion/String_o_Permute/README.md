# String-o-Permute

## Problem Statement

One very good day, Kazama gave Shinchan a string of even length, and asked him to swap the characters at even position with the next character. Indexing starts from 0.

Formally, given a string str of length L, where L is even, Shinchan has to swap the characters at position i and i+1, where i ∈ {0, 2,.., L-2}.

For example, if str = "abcdpqrs", then we have to swap the characters at position {(0, 1), (2, 3), (4, 5), (6, 7)} as L = 8. So answer will be "badcqpsr".

## Input
First line will contain an integer, T, which is the number of test cases to follow. Then follows T lines, each containing the string str.

## Output
For each test case, create the new string as mentioned above and print it.

## Constraints
```
1 ≤ T ≤ 10
str consists of lower-case latin characters, i.e., {a..z}.
1 < L ≤ 105
L is even
```
## Sample Input
```
2
abcdpqrs
az
```
## Sample Output
```
badcqpsr
za
```
## Explanation
Test case #00: This is the same example as mentioned in statement.
Test case #01: Here L is 2, so we have to swap characters at position (0, 1) only.
