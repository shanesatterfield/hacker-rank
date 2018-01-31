"""
Algorithms -> Warmup -> Birthday Cake Candles

You are in-charge of the cake for your niece's birthday and have decided the
cake will have one candle for each year of her total age. When she blows out
the candles, she’ll only be able to blow out the tallest ones. Your task is
to find out how many candles she can successfully blow out.

For example, if your niece is turning  years old, and the cake will have 4
candles of height 3, 2, 1, 3, she will be able to blow out  candles
successfully, since the tallest candle is of height 3 and there are 2 such
candles.

Complete the function birthdayCakeCandles that takes your niece's age and an
integer array containing height of each candle as input, and return the number
of candles she can successfully blow out.
"""

from typing import List


def main():
    age = int(input().strip())
    candle_heights = list(map(int, input().strip().split(' ')))
    print(birthday_cake_candles(age, candle_heights))


def birthday_cake_candles(age: int, candle_heights: List[int]) -> int:
    largest = candle_heights[0]
    count = 0

    for candle in candle_heights:
        if candle > largest:
            largest = candle
            count = 1
        elif candle == largest:
            count += 1

    return min(count, age)


if __name__ == '__main__':
    main()
