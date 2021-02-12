# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 03:05:44 2021

@author: 王泓文
"""

#Day2 tips calculaion
print("Welcome to the calculator")
bill = input("How much is the total bill? $")
tips = input("How much percentage you want to give as tips? 10, 12 or 15?")
person = input("How many person will split this bill?")
tips  = int(tips) / 100
result = ( float(bill) * (1 + tips) ) / int(person)
result = round(result, 2)
result = "{:.2f}".format(result)
print("Each person should pay $ "+ result)
