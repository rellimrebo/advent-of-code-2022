# 2

# A (1) X(24): Rock
# B (2) Y(25): Paper
# C (3) Z (26): Scissors

# Apply -23 to player inputs

# Scissors beats paper (3,2) = 5
# Paper beats rock (2, 1) = 3
# Rock beats scissors (1, 3) = 4

# Scissors draw scissors (3, 3) = 6
# Paper draws paper (2, 2) = 4
# Rock draws rock (1,1) = 2

import os

os.system('cls')

with open("2/2.txt") as f:

    score = 0

    loss_cases = [(3,2),(2,1),(1,3)]

    for line in f.readlines():
        opponent_answer, player_answer = [(ord(i) - 64) for i in line.split()]
        player_answer -= 23

        sum = opponent_answer + player_answer

        if opponent_answer == player_answer:
            score += 3

        elif (opponent_answer,player_answer) in loss_cases:
            pass

        else:
            score +=6

        score += player_answer
    
    print(score)