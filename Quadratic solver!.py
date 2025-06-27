import math
import time
##By Damoon Abdar Esfahani (DA)
print("Welcome to Quadratics solver!, you have to enter 3 co-efficients: a, b, and c")
time.sleep(1)
print("In your quadratic equation you will have 3 variables, (a,b,c), ill show you an example and tell you what the a, b, and c are)!")
time.sleep(.5)
print("For example, 3x² + 4x - 5, here a = 3, b = 4, c = -5")
time.sleep(.5)
a = float(input("Please enter your a = "))
b = float(input("Please enter your b = "))
c = float(input("Please enter your c = "))
time.sleep(1)
print("Solving!")

discriminant = b**2 - (4 * a * c)
discriminant = float(discriminant)
if discriminant > 0:
    x1 = (-b + math.sqrt(discriminant)) / (2 * a)
    x2 = (-b - math.sqrt(discriminant)) / (2 * a)
    print(f"Your 2 results are: '{x1}' and '{x2}' ")

elif discriminant < 0:
    print("There are no real roots!")

elif discriminant == 0:
    x = -b / (2 * a)
    print(f"There is one real root: {x}")

else:
    print("Please retry.")



