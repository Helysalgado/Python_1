## ---------------------------
##
## Script name: class.nucleotides.counts
##
##
## Author: Bernardo Chombo Álvarez
##
## Date Created: 2023-04-17
##
## Copyright (c) Bernardo, Chombo-Álvarez 2023
## Email: bchombo@lcg.unam.mx
##
## ---------------------------
##
## Notes: This is an interactive script that allows the user to play 'rock-scissors-paper' game vs. the computer. The game is of 2 out of 3 wins
##
## IMPORTANT: No complementary files. 
##
## ---------------------------

import random
import os

win = 0
lose = 0
i = 0

print('Please enter yout option to play:\n')
print('\ta. piedra\n\tb. papel\n\tc. tijera')

#loop with two conditions: no more than 2 wins and no more than 2 losts.
while win < 2 and lose < 2:
    i += 1
    options = ['piedra','papel','tijera']

    print(f'\n**NOW PLAYING GAME {i}')

    choice = input().rstrip("\n")

    #Set the variable 'response' to a random value contained inside list
    response = random.choice(options)
    
    #First checking that the input is done correctly
    if choice not in options:
        print('\n\t***INVALID GAME FEATURE***')
        print('Quiting game...')
        break

    #If it is not a tie, then all options display
    elif response != choice:

        #Program evaluates according to 'response' variable. In every possible game, there are only 3 options: a tie, win or lose; so it starts with loosing option, followed by winning option
        match response:
            case 'piedra':
                if choice == 'tijera':
                    lose += 1
                    print(f'Computer choice:\t{response}')
                    print(f'Your choice:\t\t{choice}')
                    print(f'FINAL RESULT:\t\tPERDISTE')
                else:
                    win += 1
                    print(f'Computer choice:\t{response}')
                    print(f'Your choice:\t\t{choice}')
                    print(f'FINAL RESULT:\t\tGANASTE')
            case 'tijera':
                if choice == 'papel':
                    lose += 1
                    print(f'Computer choice:\t{response}')
                    print(f'Your choice:\t\t{choice}')                
                    print(f'FINAL RESULT:\t\tPERDISTE')
                else:
                    win += 1
                    print(f'Computer choice:\t{response}')
                    print(f'Your choice:\t\t{choice}')                
                    print(f'FINAL RESULT:\t\tGANASTE')
            case 'papel':
                if choice == 'piedra':
                    lose += 1
                    print(f'Computer choice:\t{response}')
                    print(f'Your choice:\t\t{choice}')                
                    print(f'FINAL RESULT:\t\tPERDISTE')
                else:
                    win += 1
                    print(f'Computer choice:\t{response}')
                    print(f'Your choice:\t\t{choice}')                
                    print(f'FINAL RESULT:\t\tGANASTE')                    
    
    #Implementing tie option
    else:
        print(f'Computer choice:\t{response}')
        print(f'Your choice:\t\t{choice}')                
        print(f'FINAL RESULT:\t\tEMPATE')

#Printing all the results
print('\n**FINAL RESULTS**')
if win > lose:
    print('CONGRATULATIONS! YOU WON')
else:
    print('SORRY FELLA, YOU LOST')
print(f'wins ->\t\t{win}')
print(f'losts ->\t{lose}')


