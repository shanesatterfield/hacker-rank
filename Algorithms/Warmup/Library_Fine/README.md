# Library Fine

## Problem Statement

The Head Librarian at a library wants you to make a program that calculates the fine for returning the book after the return date. You are given the actual and the expected return dates. Calculate the fine as follows:

1. If the book is returned on or before the expected return date, no fine will be charged, in other words fine is 0.
2. If the book is returned in the same calendar month as the expected return date, Fine = 15 Hackos × Number of late days
3. If the book is not returned in the same calendar month but in the same calendar year as the expected return date, Fine = 500 Hackos × Number of late months
4. If the book is not returned in the same calendar year, the fine is fixed at 10000 Hackos.

## Input Format

You are given the actual and the expected return dates in D M Y format respectively. There are two lines of input. The first line contains the D M Y values for the actual return date and the next line contains the D M Y values for the expected return date.

## Constraints
```
1 ≤ D ≤ 31
1 ≤ M ≤ 12
1 ≤ Y ≤ 3000
```
## Output Format

Output a single value equal to the fine.

## Sample Input
```
9 6 2015
6 6 2015
```
## Sample Output
```
45
```
## Explanation

Since the actual date is 3 days later than expected, fine is calculated as 15×3=45 Hackos.
