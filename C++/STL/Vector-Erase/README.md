# Vector-Erase

## Problem Statement

You are given N integers.Then you are given 2 queries.First query consists of 1 integer denoting the position which should be removed.Next query consists of 2 integers denoting the range that should be removed.
Some more functions of vector are:

- `erase(int position):`
Removes the element present at position.<br>
Ex: v.erase(v.begin()+4); (erases the `$5{th}$` element of the vector v)

- `erase(int start,int end):`
Removes the elements in the range from start to end inclusive of the start and exclusive of the end.
Ex:v.erase(v.begin()+2,v.begin()+5);(erases all the elements from the third element to the fifth element.)

## Input Format

The first line of the input contains an integer N.The next line contains N space separated integers.The third line contains a single integer x,denoting the position of an element that should be removed from the vector.The fourth line contains two integers a and b denoting the range that should be erased from the vector inclusive of a and exclusive of b.


## Constraints
```cpp
1 <= N <= 105
1 <= x <= N
1 <= a <= b <= N−1
```
## Output Format

Print the size of the vector in the first line and the elements of the vector after the two erase operations in the second line separated by space.

## Sample Input
```cpp
6
1 4 6 2 8 9
2
2 4
```
## Sample Output
```cpp
3
1 8 9
```
