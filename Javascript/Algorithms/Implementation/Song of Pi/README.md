# Song of Pi



## Problem Statement

Today is a special day, and let me sing a song to celebrate the day:

"Now, I wish I could recollect pi.
'Eureka,' cried the great inventor.
Christmas Pudding, Christmas Pie
Is the problem's very center."

Well, you may say it's a terrible song - but it's not! Ignore the punctuation marks and write down the length of each of word in this song.

For example:

    "Now"=3, "I"=1, "wish"=4, etc etc

Writing them together we get:
314159265358979323846

That's the value of pi! (Ignoring the floating point) A song is a pi song if the length of its words represent the value of pi.

Today, March 14, is the official Pi Day because 3/14 represents the first three significant digits of Pi. And today you will determine which songs are pi songs and which are not.

Assume that value of pi is 3.1415926535897932384626433833. You don't need more digits for this problem; use the value exactly as it is, just ignore the floating point and don't perform any rounding operations.

## Input Format

The first line will contain an integer T, representing the number of test cases. Each of the next T lines will contain a song. The songs will contain only English letters (a-z, A-Z) and will contain 1 to 29 words.

## Constraints:

- No line will contain a total of more than_ 500 _characters.
- 1≤T≤100
- Length of each word is at most 9.

## Output Format

For each test case, print "It's a pi song." or "It's not a pi song." depending on the input.

## Sample Input
```
3
Can I have a large container of coffee right now
Can I have a large container of tea right now
Now I wish I could recollect pi Eureka cried the great inventor Christmas Pudding Christmas Pie Is the problems very center
```

## Sample Output
```
It's a pi song.
It's not a pi song.
It's a pi song.
```

## Explanation

If you write down the length of the words in the first case, you will get "3141592653" because length of "can"=3, "I"=1, "have"=4 etc etc. This is clearly the first few digits of Pi.

In the second case you will get "3141592353", which is wrong if you observe it carefully.

The third case is already explained in the problem statement, but here we removed all the punctuation marks to make your job easier!
