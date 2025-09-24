"""
Day 16 - Rock Paper Scissors Game
Author: Momina (shadowMomina)
Description:
A simple console-based Rock, Paper, Scissors game where the user plays
against the computer. The game tracks scores until the user decides to quit.
"""

import random  # for the computer's random choice

# All valid choices
choices = ["rock", "paper", "scissors"]

# Scores
user_score = 0
computer_score = 0

print("🎮 Welcome to Rock, Paper, Scissors Game! 🎮")
print("Type 'quit' anytime to end the game.")
print("----------------------------------------")

# Main game loop
while True:
    # Get the user's choice
    user_choice = input("\nEnter rock, paper, or scissors: ").lower()

    # Check if the user wants to quit
    if user_choice == "quit":
        print("\nThanks for playing!")
        print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
        break

    # Validate the input
    if user_choice not in choices:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Computer randomly selects a choice
    computer_choice = random.choice(choices)

    print(f"Computer chose: {computer_choice}")

    # Decide the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win this round! 🎉")
        user_score += 1
    else:
        print("Computer wins this round! 🤖")
        computer_score += 1

    # Show current scores
    print(f"Score -> You: {user_score} | Computer: {computer_score}")
