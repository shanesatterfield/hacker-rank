# For Loop

## Problem Statement

A for loop is a programming language statement which allows code to be repeatedly executed.

The syntax for this is
```cpp
for ( <expression_1> ; <expression_2> ; <expression_3> )
    <statement>
```
where any of the expressions can be ignored.

- expression_1 is used for intializing variables which are generally used for controlling terminating flag for the loop.
- expression_2 is used to check for the terminating condition. If this evaluates to false, then the loop is terminated.
- expression_3 is generally used to update the flags/variables.

A sample loop will be
```cpp
for(int i = 0; i < 10; i++) {
    ...
}
```
## Input Format

You will be given two positive integers, a and b (a≤b), separated by a newline.

## Output Format

For each integer n∈[a,b] (so all numbers in that range):

- If 1≤n≤9, then print the English representation of it. That is "one" for 1, "two" for 2, and so on.
- Else if n>9 and it is even, then print "even".
- Else if n>9 and it is odd, then print "odd".

Note: [a,b] represents the interval, i.e., [a,b]={x∈Z| a≤x≤b}={a, a+1,…,b}

## Sample Input
```
8
11
```
## Sample Output
```
eight
nine
even
odd
```
