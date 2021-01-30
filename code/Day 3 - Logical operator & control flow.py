# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:44:51 2021

@author: 王泓文
"""

#Day 3 - Logical operator & control flow
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

name1 = name1.lower()
name2 = name2.lower()

love = 'love'
true = 'true'
decimal = 0
unit = 0

for i in name1:
  for j in true:
    if j == i:
      decimal +=1

for i in name2:
  for j in true:
    if j == i:
      decimal +=1


for i in name1:
  for j in love:
    if j == i:
      unit +=1

for i in name2:
  for j in love:
    if j == i:
      unit +=1

love_point = decimal*10 + unit

if love_point<=10 or love_point>=90:
  print (f"Your score is {love_point}, you go together like coke and mentos.")
elif love_point>=40 and love_point<=50:
  print(f"Your score is {love_point}, you are alright together.")
else:
  print(f"Your score is {love_point}.")
