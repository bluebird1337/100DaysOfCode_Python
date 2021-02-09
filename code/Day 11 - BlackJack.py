# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 19:29:03 2021

@author: 王泓文
"""

"""
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
"""

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
from os import system, name
def clear(): 

    if name == 'nt': 
        _ = system('cls') 
        
import random
                  
play = str(input("Do you want to play a game of Blackjyack? Type 'y' or 'n':"))
start = True
if(play == 'n') : 
    start = False
while start:
    print(logo)
    user_deck = random.choices(cards, weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], k = 2)
    user_score = 0
    for point in user_deck:
        user_score += point
    computer_deck = []
    computer_score = random.choice(cards)
    computer_deck.append(computer_score)
    print(f"Your cards : {user_deck}, current score : {user_score}")
    print(f"Computer's first card : {computer_score}")
    another_card = str(input("Type 'y' to get another card, type 'n' to pass:"))
    get_new_card = True
    if(another_card == 'n'):
        get_new_card = False
    while(get_new_card):
        new_card = random.choice(cards)
        user_deck.append(new_card)
        user_score += new_card
        if(user_score>21):
            break
        print(f"Your cards : {user_deck}, current score : {user_score}")
        print(f"Computer's first card : {computer_score}")
        another_card = str(input("Type 'y' to get another card, type 'n' to pass:"))    
        if(another_card == 'n'):
            get_new_card = False
    #Conclude
    if user_score>21: # Explode
        print(f"Your final cards : {user_deck}, final score : {user_score}")
        print("You went over. You lose 😭")
    else: # Not explode
        while computer_score<17:
            new_card = random.choice(cards)
            computer_deck.append(new_card)
            computer_score += new_card
        if(computer_score>21):
            print(f"Your final cards : {user_deck}, final score : {user_score}")
            print(f"Computer's final cards : {computer_deck}, final score : {computer_score}")
            print("Opponent went over, You win !!")
        else:
            if(computer_score == user_score):
                print(f"Your final cards : {user_deck}, final score : {user_score}")
                print(f"Computer's final cards : {computer_deck}, final score : {computer_score}")
                print("Draw!!")
            elif(computer_score > user_score):
                print(f"Your final cards : {user_deck}, final score : {user_score}")
                print(f"Computer's final cards : {computer_deck}, final score : {computer_score}")
                print("You lose 😭")
            else:
                print(f"Your final cards : {user_deck}, final score : {user_score}")
                print(f"Computer's final cards : {computer_deck}, final score : {computer_score}")    
                print("You win !!")
                
    play = str(input("Do you want to play a game of Blackjack? Type 'y' or 'n':"))
    if(play == 'n') : 
        start = False
#Not Enter / End the game
clear()    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    