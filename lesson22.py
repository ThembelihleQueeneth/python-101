
import random

# Store all the possible choices in a list
choices = ["rock", "paper", "scissors"]

# Let the computer randomly choose rock, paper, or scissors
computer = random.choice(choices)

# Ask the player to enter their choice
player = input("Choose rock, paper, or scissors: ").lower()

# Display the choices made by the player and computer
print("You chose:", player)
print("Computer chose:", computer)

# Check if the player entered an invalid choice
if player not in choices:
    print("Invalid choice! Try again.")

# Check if both chose the same thing
elif player == computer:
    print("It's a tie!")

# Check if the player wins
elif (player == "rock" and computer == "scissors") or \
     (player == "paper" and computer == "rock") or \
     (player == "scissors" and computer == "paper"):
    print("Congratulations! You win!")

# If the player did not win or tie, the computer wins
else:
    print("Sorry, the computer wins!")
