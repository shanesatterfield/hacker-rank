# Filter Array

## Problem Statement

Filter a given array of integers and leave only that values which are less than a specified value X. The integers in the output should be in the same sequence as they were in the input. You need to write a function with the recommended method signature for the languages mentioned below. For rest of language you have to write complete code.

## Input Format
The first line contains the delimiter X. This is followed by a list of integers, which represents the elements of list/array. You have to read input to the End-Of-File.

## Output Format
Print integers in separate line from the array which are less than an upper-limit X in value. The sequence should be same as it was in the original array.

## Constraints
```
1 <= size of array <= 100
For any element in the array, say Y, -100 <= Y <= 100
-100 <= X <= 100
```

## Note
You have to write your own implementation of filter function. It is recommended to not use inbuilt library function.

## Sample Input
```
3
10
9
8
2
7
5
1
3
0
```
## Sample Output
```
2
1
0
```
## Explanation
2, 1, 0 are the members of the list which are less than the delimiter (3). Also, they are displayed in the same order as they were in the original list.

## Recommended Method Signature
```
Number Of Parameters: 2
Parameters: [upper-limit(X) list]
Returns: List or Vector
```
