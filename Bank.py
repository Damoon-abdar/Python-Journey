##Bank investment project by DA
## In this program i tried to offer the customer a principal protected Note strategy
## I'll try to make this code more complicated and fetch real time bank data in the future :)

import time
import sys
import math
name = input("You have reached M&J bank. Please enter in your name: ")
dob = input(f"Please enter your age {name}. : ")
dob = float(dob)
dob = round(dob)
if dob < 18:
    print("You are not eligible for any investments until you are 18. We apologize for any inconvenience.")
    sys.exit()
else:
    print("Great!")
time.sleep(1)
PPN = input("We offer a Principal-Protected Note investment strategy. Would you like to know more? (Y/N): ")
if PPN == "Y" or "y" or " Y" or " y":
    print("Perfect.")
elif PPN == "N" or "n" or " n" or " N":
    print("No problem, Thanks for your time.")
    sys.exit()

print(f"{name}, We offer PPN investments at yearly returns of 10%, if you'd like to get a quick calculation of how much you'll be recieving from your investment you can enter our quick calculator.")
time.sleep(.7)
calc = input("Please enter the amount you're looking to invest: ")
calc = float(calc)
PPN_return1 = calc * (10/100)
finalc = PPN_return1 + calc
finalc = float(finalc)
finalc = round(finalc)
print(f"Your profit would be: {PPN_return1}, so your initial amount was {round(calc)} and your final would be {finalc}")