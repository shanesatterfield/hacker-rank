# Finding the Percentage

## Problem Statement

There is a record of 'n' students, each record having name of student, percent marks obtained in Maths, Physics and Chemistry. Marks can be floating values. The user enters an integer 'n' followed by names and marks for the 'n' students. You are required to save the record in a dictionary data type. The user then enters name of a student and you are required to print the average percentage marks obtained by that student, correct to two decimal places.

## Input Format

Integer N followed by name and marks for N students, followed by the name of the particular student.

## Output Format

Average percentage of marks obtained

## Constraints
2 <= N <= 10
0 <= Marks <= 100

## Sample Input
```
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
```
## Sample Output
```
56.00
```
## Concept

Dictionary is a data-type which stores values in pairs i.e. to say for each element in the dictionary there is a unique key and value that the key points to. Dictionary is a mutable.
Eg:
```python
>> a = {'one': 1} # Here 'one' is the key.
Note : Key of a dictionary is immutable. So, we can't use list as a key as list is mutable.
>> a['two'] = 2 # Adds key 'two' which points to 2
>> a['one']
1
>> if ('three' in a): # To check whether a certain string exist as index in dictionary
.. print a['three']
.. else:
.. print "Three not there"
Three not there
>> del a['one'] # Deletes index 'one' and value associated with it
>> a
{'two': 2}
```
Note : Dictionary is an unordered. So, only use index to navigate through the dictionary.
