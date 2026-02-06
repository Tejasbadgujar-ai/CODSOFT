# ================================
# ROCK-PAPER-SCISSORS GAME
# ================================
# This program allows the user to:
# 1. Choose rock, paper, or scissors
# 2. Computer randomly chooses
# 3. Decide winner
# 4. Option to play again

import random

choices = ["rock", "paper", "scissors"]

while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        print("You win!")
    else:
        print("You lose!")

    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        break