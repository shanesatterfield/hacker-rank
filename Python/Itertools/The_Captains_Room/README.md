# The Captain's Room

## Problem Statement

Mr. Anant Asankhya is the manager at INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists came to stay at the hotel.
Tourists consisted of :  
→ a Captain.  
→ Equal sized group of families (size K each and K ≠ 1).

The Captain was given a separate room and rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of room numbers of all the tourists. The room numbers will appear K times per group except for the Captain's room.

Mr. Anant needs help from you to find the Captain's room number.
Total number of Tourists or total group of families is not known to you.
You only have the value of K and room number list.

## Input Format

First line consists of K (The size of each group).
Second line consists of room number list.


## Constraints
```
1<K<1000
```
## Output Format

Output the Captain's room number.

## Sample Input
```
5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2
```
## Sample Output
```
8
```
## Explanation

In the given list all the numbers repeat 5 times except room number 8.
Hence, 8 is the Captain's room number.
