from __future__ import print_function
import sys

times = {
     1: 'one minute',
     2: 'two minutes',
     3: 'three minutes',
     4: 'four minutes',
     5: 'five minutes',
     6: 'six minutes',
     7: 'seven minutes',
     8: 'eight minutes',
     9: 'nine minutes',
    10: 'ten minutes',
    11: 'eleven minutes',
    12: 'twelve minutes',
    13: 'thirteen minutes',
    14: 'fourteen minutes',
    15: 'quarter',
    16: 'sixteen minutes',
    17: 'seventeen minutes',
    18: 'eighteen minutes',
    19: 'nineteen minutes',
    20: 'twenty minutes',
    21: 'twenty one minutes',
    22: 'twenty two minutes',
    23: 'twenty three minutes',
    24: 'twenty four minutes',
    25: 'twenty five minutes',
    26: 'twenty six minutes',
    27: 'twenty seven minutes',
    28: 'twenty eight minutes',
    29: 'twenty nine minutes',
    30: 'half'
}

hour_words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
   10: 'ten',
   11: 'eleven',
   12: 'twelve',
}

def word_time(hours, minutes):
    min_word = 60 - minutes if minutes > 30 else minutes
    if minutes == 0:
        return hour_words[hours] + " o' clock"

    words = times[min_word]
    if minutes <= 30:
        words += ' past ' + hour_words[hours]
    else:
        words += ' to ' + hour_words[hours+1]

    return words


def main():
    hours, minutes = [ int(x.strip()) for x in sys.stdin.readlines()[:2] ]
    print(word_time(hours, minutes))

if __name__ == '__main__':
    main()
