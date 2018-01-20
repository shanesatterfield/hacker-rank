# BotClean Large

## Problem Statement

The goal of Artificial Intelligence is to create a rational agent (Artificial Intelligence 1.1.4). An agent receives input from the environment through sensors and acts on the environment using actuators. In this challenge, you will program a simple bot to perform the correct actions based on environmental input.

Meet the bot MarkZoid - a floor cleaning bot with a head mounted camera (sensor) and wheels (actuator) that help move it.

The bot is positioned at a cell in a H*W grid. Your task is to move the bot so that it cleans all the dirty cells.

## Input Format

The first line contains two space separated integers which indicate the current x,y position of the bot. The board is indexed using Matrix Convention.

The next line contains two space separated integers H and W (1 <= H, W <= 50) which indicate the size of the board.

H lines follow representing the grid. Each cell in the grid is represented by any of the following 3 characters:
- 'b' (ascii value 98) indicates the bot's current position,
- 'd' (ascii value 100) indicates a dirty cell and
- '-' (ascii value 45) indicates a clean cell in the grid.
If the bot is on a dirty cell, 'd' will be printed in that location.

## Output Format

The output is the action taken by the bot in the current step. The action can be LEFT, RIGHT, UP and DOWN or CLEAN. A direction denotes movement in the respective direction. And CLEAN denotes the cleaning action performed when the bot reaches a dirty cell. These actions are repeated until all the cells on the grid are cleaned.

## Sample Input
```
0 0
5 5
b---d
-d--d
--dd-
--d--
----d
```
## Sample Output

RIGHT
## Resultant state
```
-b--d
-d--d
--dd-
--d--
----d
```
## Task

Complete the function next_move that takes in 5 parameters:
posr, posc are the co-ordinates of the bot's current position,
(row, column), dimh, dimw are the height and the width of the board respectively and
board indicates the board state to print the bot's next move. board will be an array of strings.

## Scoring

Your score is (200 - number of moves the bots make) /10. CLEAN is also considered a move. All boards can be cleaned in less than 200 moves and you cannot get a negative score.

Once you submit, your bot will be played on four grids with three of the grid configurations unknown to you. The final score will be the sum of your scores in each of the four grids.

## Education Links

Introduction to AI by Stuart Russell and Peter Norvig
Motor cognition
