# String Compression

## Problem Statement

Joseph and Javran are making a contest for the apes. During the process they have to communicate frequently with each other. Since they are not fully evolved as humans, they cannot speak properly. So they have to transfer messages using postcards of small sizes.
To save space on the small postcards, they devise a not-so-uncommon string compression algorithm:

If a character, ch, occurs n(>1) times in a row, then it will be represented by {ch}{n}, where {x} is the value of x. For example, if the substring is a sequence of 4 'a' ("aaaa"), it will be represented as "a4".

If a character, ch, occurs exactly one time in a row, then it will be simply represented as {ch}. For example, if the substring is "a", then it will be represented as "a".

Help Joseph to compress a message, msg, which will be sent to Javran.

## Input
First, and only, line contains a string, msg, representing the message.

## Output
Print the compressed message.

## Constraints
```
1≤length(msg)≤105
```
msg consists of lowercase Latin characters ('a'-'z') only.
## Sample Input \#00
```
abcaaabbb
```
## Sample Output \#00
```
abca3b3
```
## Sample Input \#01
```
abcd
```
## Sample Output \#01
```
abcd
```
## Sample Input \#02
```
aaabaaaaccaaaaba
```
## Sample Output \#02
```
a3ba4c2a4ba
```
## Explanation
Sample Case #00: msg = "abcaaabbb". Here first 3 characters occurs exactly once, and rest of them occur 3 times in a sequence.
Sample Case #01: msg = "abcd". As there is no multiple consecutive occurrence of any character, compressed message will be same as original one.
Sample Case #02: msg = "aaabaaaaccaaaaba". In first 3 occurrence 'a' is repeated 4 times, while in last occurrence only one a is there. While 'c' occurs two times, and 'b' occurs one time in both occurrence.
