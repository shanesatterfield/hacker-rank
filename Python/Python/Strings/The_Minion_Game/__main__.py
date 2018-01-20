from __future__ import print_function
import sys

vowels = ['a','e','i','o','u']
player = ['Draw', 'Stuart', 'Kevin']

def minion(text):
    text = text.lower()
    players = [[player[1],0],[player[2],0]]
    for i in range(len(text)):
        curr_player = int(text[i] in vowels)
        players[curr_player][1] += len(text) - i

    if players[0][1] == players[1][1]:
        return [player[0]]
    return max(players, key=lambda x: x[1])

def main():
    print(*minion(sys.stdin.read().rstrip()))

if __name__ == '__main__':
    main()
