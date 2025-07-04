import time
import math

##this game is a guessing game

print("Hello! We'll be asking 3 questions about common knowledge.")
q1 = input("What's the biggest country in the world? : ")
if q1 == "Russia" or "russia" or "RUSSIA":
    print("Great! Correct.")
else:
    print("Wrong.")
q2 = input("What's the first 3 digits of pi? :  ")
if q2 == "3.14":
    print("Great!")
else:
    print("Incorrect :(")
q3 = input("What's the name of the scientist who invented the light bulb? : ")
if q3 == "Thomas edison" or "THOMAS EDISON" or "Thomas Edison" or "thomas edison":
    print('Perfect!')
else:
    print("Incorrect")
