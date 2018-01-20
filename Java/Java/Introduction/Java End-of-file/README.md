# Java End-of-file

## Problem Statement

> In computing, End Of File (commonly abbreviated EOF) is a condition in a computer operating system where no more data can be read from a data source. (Wikipedia)

Sometimes you don't know how many lines are there in a file and you need to read the file until EOF or End-of-file. In this problem you need to read a file until EOF and print the contents of the file. You must take input from stdin(System.in).

Hints: One way to do this is to use hasNext() function in java scanner class.

## Input Format

Each line will contain a non-empty string. Read until EOF.

## Output Format

For each line, print the line number followed by a single space and the line content.

## Sample Input
```
Hello world
I am a file
Read me until end-of-file.
```
## Sample Output
```
1 Hello world
2 I am a file
3 Read me until end-of-file.
```
