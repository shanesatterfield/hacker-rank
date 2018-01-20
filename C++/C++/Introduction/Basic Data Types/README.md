# Basic Data Types

## Problem Statement

C++ has the following data types along with their format specifier:

    Int ("%d"): 32 Bit integer
    Long (%ld): 32 bit integer (same as Int for modern systems)
    Long Long ("%lld"): 64 bit integer
    Char ("%c"): Character type
    Float ("%f"): 32 bit real value
    Double ("%lf"): 64 bit real value

## Reading
In order to read a data type, you need the following syntax:
```
scanf("`format_specifier`", &val)
```
E.g., in order to read a character and then a double
```
char ch;
double d;
scanf("%c %lf", &ch, &d);
```
P.S.: For the moment, we can ignore the spacing between format specifiers.

## Printing
In order to print a data type, you need the following syntax:
```
printf("`format_specifier`", val)
```
E.g., in order to print a character and then a double
```
char ch = 'd';
double d = 234.432;
printf("%c %lf", ch, d);
```
P.S.: For the moment, we can ignore the spacing between format specifiers.

## Input Format

Input will consists of an int, long, long long, char, float and double, each separated by a space.

## Output Format

Print the elements in the same order, but each in a new line.

## Sample Input
```
3 444 12345678912345 a 334.23 14049.30493
```
## Sample Output
```
3
444
12345678912345
a
334.23
14049.30493
```
