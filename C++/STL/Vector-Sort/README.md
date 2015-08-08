# Vector-Sort

## Problem Statement

You are given N integers.Sort the N integers and print the sorted order.
Store the N integers in a vector.Vectors are sequence containers representing arrays that can change in size.

- Declaration:
```cpp
vector<int>v; (creates an empty vector of integers)
```

- Size:
```cpp
int size=v.size();
```

- Pushing an integer into a vector:
```cpp
v.push_back(x);(where x is an integer.The size increases by 1 after this.)
```

- Popping the last element from the vector:
```cpp
v.pop_back(); (After this the size decreases by 1)
```

- Sorting a vector:
```cpp
sort(v.begin(),v.end()); (Will sort all the elements in the vector)
```

To know more about vectors, [Click Here](http://www.cplusplus.com/reference/vector/vector/)

## Input Format

The first line of the input contains N where N is the number of integers. The next line contains N integers.
Constraints
```
1<=N<=105
1<=Vi<=109, where Vi is the ith integer in the vector.
```
## Output Format

Print the integers in the sorted order one by one in a single line followed by a space.

## Sample Input
```
5
1 6 10 8 4
```
## Sample Output
```
1 4 6 8 10
```
