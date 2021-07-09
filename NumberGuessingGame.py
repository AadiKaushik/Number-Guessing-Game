
import random

chances = 0
randomNumber = round(random.uniform(0,9))

print('Number Guessing Game')

while chances < 5:

    userGuess = input('Enter Your Guess')
    

    if(str(randomNumber) == userGuess):
     print('Congratulation!!you won')
     chances = 6

    else:
        chances = chances +1
        if(str(randomNumber) > userGuess ):
            print('Guess a number higher than ',userGuess )
        elif(str(randomNumber) < userGuess ):
            print('Guess a number lower than ',userGuess )    
    if(chances == 5):
        print('The Number was ',randomNumber)        