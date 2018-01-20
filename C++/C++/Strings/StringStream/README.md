# StringStream

## Problem Statement

stringstream is a stream class to operate on strings. It basically implements input/output operations on memory (string) based streams. stringstream can be helpful in different type of parsing. The following operators/functions are commonly used here
```
Operator >> Extracts formatted data.
Operator << Inserts formatted data.
Method str() Gets the contents of underlying string device object.
Method str(string) Sets the contents of underlying string device object.
```
Its header file is sstream.

One common use of this class is to parse comma-separated integers from a string (e.g., "23,4,56").
```cpp
stringstream ss("23,4,56");
char ch;
int a, b, c;
ss >> a >> ch >> b >> ch >> c;  // a = 23, b = 4, c = 56
```
You have to complete the function vector parseInts(string str). str will be a string consisting of comma-separated integers, and you have to return a vector of int representing the integers.

## Input Format

The first and only line consists of n comma-separated integers.

## Output Format

Print the integers after parsing it.

P.S.: I/O will be automatically handled. You need to complete the function only.

## Sample Input
```
23,4,56
```
## Sample Output
```
23
4
56
```
