# Conditional Statements

## Problem Statement

if and else are two of the most heavily used conditionals in C/C++. They are used to execute zero or one statement among many statements.

They are be used in the following three ways.

1. if: It is used to execute a statement, given the condition is true.
```cpp
if(condition) {
    ...
}
```
2. if - else: It is used to execute exactly one of the two statements.
```cpp
if(first condition) {
    ...
}
else {
    ...
}
```
3. if - else if - else: It is used to execute one of the multiple statements.

```cpp
if(first condition) {
    ...
}
else if(second condition) {
    ...
}
.
.
.
else if((n-1)'th condition) {

}
else(n'th condition) {
    ...
}
```
You are given a positive integer, n,:

- If 1≤n≤9, then print the English representation of it. That is "one" for 1, "two" for 2, and so on.
- Otherwise print "Greater than 9" (without quotes).

## Input Format

Input will contain only one integer, n.

## Output Format

Print the output as described above.

## Sample Input
```
5
```
## Sample Output
```
five
```
## Sample Input \#01
```
8
```
## Sample Output \#01
```
eight
```
## Sample Input \#02
```
44
```
## Sample Output \#02
```
Greater than 9
```
