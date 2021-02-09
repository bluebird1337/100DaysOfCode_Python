# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 23:16:56 2021

@author: 王泓文
"""


import random
logo ="""                                                                                                                                                                                                                                                                                                                                              
,--.  ,--.                  ,--.                      ,----.                                ,--.                    ,----.                             
|  ,'.|  |,--.,--.,--,--,--.|  |-.  ,---. ,--.--.    '  .-./   ,--.,--. ,---.  ,---.  ,---. `--',--,--,  ,---.     '  .-./    ,--,--.,--,--,--. ,---.  
|  |' '  ||  ||  ||        || .-. '| .-. :|  .--'    |  | .---.|  ||  || .-. :(  .-' (  .-' ,--.|      \| .-. |    |  | .---.' ,-.  ||        || .-. : 
|  | `   |'  ''  '|  |  |  || `-' |\   --.|  |       '  '--'  |'  ''  '\   --..-'  `).-'  `)|  ||  ||  |' '-' '    '  '--'  |\ '-'  ||  |  |  |\   --. 
`--'  `--' `----' `--`--`--' `---'  `----'`--'        `------'  `----'  `----'`----' `----' `--'`--''--'.`-  /      `------'  `--`--'`--`--`--' `----' 
                                                                                                        `---'                                                                                 """
print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
ans = random.randint(1, 101)
print(f"Pssst, the correct answer is {ans}")
level = input("Choose a difficulty. Type 'easy' or 'hard':")
num_of_fail = 10
if level == "hard":
  num_of_fail = 5
Got_it = False
while num_of_fail > 0 :
  print(f"You have {num_of_fail} attempts remaining to guess the number.")
  guess = int(input("Make a guess : "))
  if(guess == ans):
    print(f"You Got it !, the answer is {ans}")
    Got_it = True
    break
  elif (guess > ans):
    print("Too high")
    num_of_fail-=1
  else:
    print("Too low")
    num_of_fail-=1

if(Got_it == False):
  print("You've run out of guesses, you lose.")