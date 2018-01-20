# Little Panda Power

## Problem Statement

Little Panda has a thing for powers and modulus and he likes challenges. His friend Lucy, however, is impractical and challenges Panda to find both positive and negative powers of a number modulo a particular number. We all know that A^−1 mod X refers to the modular inverse of A modulo X (see [Wikipedia](http://en.wikipedia.org/wiki/Modular_multiplicative_inverse)).

Since Lucy is impractical, she says that A^−n mod X=(A^−1 mod X)^n mod X for n>0.

Now she wants Panda to compute A^B mod X.

She also thinks that this problem can be very difficult if the constraints aren't given properly. Little Panda is very confused and leaves the problem to the worthy programmers of the world. Help him in finding the solution.

## Input Format
The first line contains T, the number of test cases.
Then T lines follow, each line containing A, B and X.

## Output Format
Output the value of A^B mod X.

## Constraints
```
1 ≤ T ≤ 1000
1 ≤ A ≤ 10^6
−10^6 ≤ B ≤ 10^6
1 ≤ X ≤ 10^6
```
A and X are coprime to each other (see [Wikipedia](http://en.wikipedia.org/wiki/Coprime_integers))

## Sample Input
```
3  
1 2 3  
3 4 2  
4 -1 5
```
## Sample Output
```
1  
1  
4  
```
## Explanati
```
Case 1: 1^2 mod 3 = 1 mod 3 = 1
Case 2: 3^4 mod 2 = 81 mod 2 = 1
Case 3: 4^−1 mod 5 = 4
```
