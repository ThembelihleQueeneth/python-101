import random

def guess_the_number():
    # 1. The computer picks a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")

    # 2. Start a loop that runs until the user guesses correctly
    while True:
        try:
            # 3. Take input from the user and convert it to an integer
            user_guess = int(input("Take a guess: "))
            attempts += 1 # Increment the attempt counter
            
            # 4. Check if the guess is too high, too low, or correct
            if user_guess < secret_number:
                print("Too low! Try again.")
            elif user_guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"🎉 Correct! You found the number in {attempts} attempts.")
                break # Exit the loop when they win
                
        except ValueError:
            # Handle the case where the user inputs a letter instead of a number
            print("Please enter a valid valid number.")

# Run the game
guess_the_number()
