# Nested List

## Problem Statement

Now we will see how to implement a nested list. There is a classroom of 'n' students and you are given their names and marks in physics. Store them in a nested list and print the name of each student who got the second lowest marks in physics.

NOTE: If there are more than one student getting same marks, make sure you print the names of all students in alphabetical order, in different lines.

## Input Format

Integer N followed by alternating sequence of N strings and N numbers.

## Output Format

Name of student.

## Constraints
```
1≤N≤5
```
## Sample Input
```
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39
```
## Sample Output
```
Berry
Harry
```
## Concept

Lists can be nested i.e. to say that one list can contain another list.
Eg:
```python
>> a = [['blue', 'green'], ['red', 'black'], ['blue', 'white']]
>> len(a)
3
>> a[1]
['red', 'black']
>> a[1][0]
red
```
To go through every element in a list, use nested for loop.
