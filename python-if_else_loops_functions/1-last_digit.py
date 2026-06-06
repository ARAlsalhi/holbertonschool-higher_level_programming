#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
str1 = "Last digit of"
lastD = abs(number) % 10
if (number < 0):
    lastD = -lastD
if (lastD > 5):
    print (str1 +f" {number} is {lastD} and is greater than 5")
elif (lastD == 0):
    print (str1 +f" {number} is {lastD} and is 0")
elif (lastD < 6 and not 0):
    print (str1 +f" {number} is {lastD} and is less than 6 and not 0")
