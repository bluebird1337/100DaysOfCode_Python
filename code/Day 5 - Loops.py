# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 22:42:16 2021

@author: 王泓文
"""

#Day5 loops
#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_base = ""
#Generate symbols
for i in range(0, nr_symbols):
    c = symbols[random.randint(0, 8)]
    password_base = password_base + c

#Generate numbers
for i in range(0, nr_numbers):
    c = numbers[random.randint(0, 9)]
    password_base = password_base + c
#Generate letters
remain = nr_letters - nr_symbols - nr_numbers
for i in range(0, remain):
    c = letters[random.randint(0, 51)]
    password_base = password_base + c

password = ""
for i in range(0, nr_letters):
    leng = len(password_base) - 1 
    word = password_base[random.randint(0, leng)]
    password = password + word
    password_base = password_base.replace(word, "", 1)
print(password)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

for i in range(1, 101):
    if(i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif(i % 3 == 0):
        print ("Fizz")
    elif(i % 5 == 0):
        print("Buzz")
    else:
        print(i)
        

sum = 0
for i in range(2, 101, 2):
    sum += i
print (sum)

score = input("Enter the score list : ").split(" ")

for i in range(0, len(score)):
    score[i] = int(score[i])
max = score[0]
for i in range (1, len(score)):
    if(max < score[i]):
        max = score[i]
print (max)


score = input("Enter the score list : ").split(" ")
sum = 0
j = 0
for i in score:
    score[j] = int(i)
    sum += score[j]
    j += 1
print (f"sum = {sum}, j = {j}\n")
aver = round(sum / j)
print (int(aver))

