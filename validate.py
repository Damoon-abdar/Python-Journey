#validate user input exercise
#1. username is no more than 12 characters.
#2. username must not contain spaces
#3. username most not contain digits
## Inspired by brocode
import sys
import time
username = input("Dear user please enter in a username you'd like to have: ")
check = len(username)
check2 = username.count(" ")
check3 = username.isdigit()

if check > 12 or check2 > 0 or check3 :
    print("Your username has an error please restart.")
    sys.exit()
else:
    print("Great")
time.sleep(.9)

