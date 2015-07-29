# Java Output Formatting

## Problem Statement

Java System.out.printf function allows you to print formatted output. This problem will test your knowledge on this topic.

Take exactly 3 lines of input. Each line consists of a string and an integer. Suppose this is the sample input:
```
java 100
cpp 65
python 50
```
The strings will have at most 10 alphabetic characters and the integers will range between 0 to 999.

In each line of output there should be two columns. The string should be in the first column and the integer in the second column. This is the output for the input above:
```
================================
java           100
cpp            065
python         050
================================
```
The first column should be left justified using exactly 15 characters. The integer of the second column should have exactly 3 digits. If the original input has less than 3 digits, you should pad with zeros to the left.
