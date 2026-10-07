secret = 7
guesses = 0

while True:
    guess = int(input("Guess a number: "))
    guesses+=1
    
    if guess == secret :
        print('Your guess was correct')
        print(f'It took you {guesses} guesses to get the correct value')
        break
    elif guess > secret:
        print('Too High')   
    else:
        print('Too Low')     