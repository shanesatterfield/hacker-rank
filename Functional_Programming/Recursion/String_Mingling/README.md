## Problem Statement

Pawel and Shaka recently became friends. On their planet, it is believed that their friendship will last forever, if they merge their favorite strings and etch it on the surface of a stone.

So we will mingle their favorite strings. The lengths of their favorite strings is same (say n). Mingling two strings, P=p1p2…pn and Q=q1q2…qn, both of length n, will result in creation of a new string R of length 2×n. It will have the following structure:
```
R=p1q1p2q2…pnqn
```
You are given two strings P (favorite of Pawel) and Q (favorite of Shaka), find the mingled string R.

## Input
First line of input contains string P, and second line contains Q.

## Output
Print string R.


## Constraints
- 1≤n≤105
- length(P)=length(Q)=n
- String consists of only lower case Latin characters ('a'-'z').

## Sample Input \#00
```
abcde
pqrst
```
## Sample Output \#00
```
apbqcrdset
```
## Sample Input \#01
```
hacker
ranker
```
## Sample Output \#01
```
hraacnkkeerr
Explanation
```
## Sample Case \#00:
```
P=a   b   c   d   e
Q=p   q   r   s   t
R=ap bq cr ds et
```
## Sample Case \#01:
```
P=h   a   c   k   e   r
Q=r   a   n   k   e   r
R=hr aa cn kk ee rr
```
