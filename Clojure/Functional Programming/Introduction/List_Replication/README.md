# List Replication

## Problem Statement

Given a list repeat each element of the list n times. The input and output portions will be handled automatically by the grader. You need to write a function with the recommended method signature.

## Input Format
First line has integer S where S is the number of times you need to repeat elements. After this there are X lines, each containing an integer. These are the X elements of the array.

## Output Format
Repeat each element of the original list S times. So you have to return list/vector/array of S*X integers. The relative positions of the values should be same as the original list provided as input.

## Constraints
```
0 <= X <= 10
1 <= S <= 100
```
## Sample Input
```
3
1
2
3
4
```
## Sample Output
```
1
1
1
2
2
2
3
3
3
4
4
4
```
## Recommended Method Signature
```
Number Of Parameters: 2
Parameters: [number of times to replicate elements, list]
Returns: List or Vector
```
