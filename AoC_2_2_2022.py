# 2.2

import os

os.system('cls')

with open("2/2.txt") as f:

    score = 0

    for line in f.readlines():
        opponent_answer, game_condition = [(ord(i) - 64) for i in line.split()]
        game_condition -= 23
        player_answer = 0

        if game_condition == 1: # LOSE
            
            player_answer = opponent_answer - 1
            if opponent_answer == 1:
                player_answer = 3

        elif game_condition == 2: # DRAW
            score += 3
            
            player_answer = opponent_answer

        else: # WIN
            score +=6

            player_answer = opponent_answer + 1
            if player_answer == 4:
                player_answer = 1

        score += player_answer
        
    print(score)