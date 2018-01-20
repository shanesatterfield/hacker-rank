# Taum and B'day

## Problem Statement

Taum is planning to celebrate the birthday of his friend, Diksha. There are two types of gifts that Diksha wants from Taum: one is black and the other is white. To make her happy, Taum has to buy B number of black gifts and W number of white gifts.

The cost of each black gift is X units.
The cost of every white gift is Y units.
The cost of converting each black gift into white gift or vice versa is Z units.
Help Taum by deducing the minimum amount he needs to spend on Diksha's gifts.

## Input Format

The first line will contain an integer T which will be the number of test cases.
There will be T pairs of lines. The first line of each test case will contain the values of integers B and W. Another line of each test case will contain the values of integers X, Y, and Z.

## Constraints
```
1≤T≤10
0≤X,Y,Z,B,W≤109
```
## Output Format

T lines, each containing an integer: the minimum amount of units Taum needs to spend on gifts.

## Sample Input
```
5
10 10
1 1 1
5 9
2 3 4
3 6
9 1 1
7 7
4 2 1
3 3
1 9 2
```
## Sample Output
```
20
37
12
35
12
```
##Explanation

#### Sample Case #01:
There is no benefit to converting the white gifts into black or the black gifts into white, so Taum will have to buy each gift for 1 unit. So cost of buying all gifts will be: 10∗1+10∗1=20.

#### Sample Case #02:
Again, we can't decrease the cost of black or white gifts by converting colors. We will buy gifts at their original price. So cost of buying all gifts will be: 5∗2+9∗3=10+27=37.

#### Sample Case #03:
We will buy white gifts at their original price, 1. For black gifts, we will first buy white one and color them to black, so that their cost will be reduced to 1+1=2. So cost of buying all gifts will be: 3∗2+6∗1=12.

#### Sample Case #04:
Similarly, we will buy white gifts at their original price, 2. For black gifts, we will first buy white one and color them to black, so that their cost will be reduced to 2+1=3. So cost of buying all gifts will be: 7∗3+7∗2=35.

#### Sample Case #05:
We will buy black gifts at their original price, 1. For white gifts, we will first black gifts worth 1 unit and color them to white with another 2 units, so cost for white gifts is reduced to 3 units. So cost of buying all gifts will be: 3∗1+3∗3=3+9=12.
