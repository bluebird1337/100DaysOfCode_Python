# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:43:16 2021

@author: 王泓文
"""

#Day 4 Randomisation & Python Lists
rock = 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)


paper = 
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)


scissors = 
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

import random
choice = input ("What do you choose? Type 0 for stone, 1 for scissors and 2 for paper")

computer_choice = random.randint(1, 3)
computer_choice -=1
#user's choice
valid = 0
if(choice == '0'):
  print("Your choice:\n")
  valid = 1
  print (rock)
elif (choice == '1'):
  valid = 1
  print("Your choice:\n")
  print(scissors)
elif (choice == '2'):
  valid = 1
  print("Your choice:\n")
  print(paper)
else:
  print("Please Enter a valid choice")

#computer's choice
if(valid == 1):
  if(computer_choice == 0):
    print("Computer's choice:\n")
    print (rock)
  elif (computer_choice == 1):
    print("Computer's choice:\n")
    print(scissors)
  elif (computer_choice == 2):
    print("Computer's choice:\n")
    print(paper)

#result
if(valid == 1):
  if(choice=='0'):
    if(computer_choice == 0):
      print ("Tie!")
    elif(computer_choice == 1):
      print("You win!")
    else:
      print("You lose")
  if(choice=='1'):
    if(computer_choice == 1):
      print ("Tie!")
    elif(computer_choice == 2):
      print("You win!")
    else:
      print("You lose")
  if(choice=='2'):
    if(computer_choice == 2):
      print ("Tie!")
    elif(computer_choice == 0):
      print("You win!")
    else:
      print("You lose")
