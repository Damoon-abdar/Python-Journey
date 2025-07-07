#lists
#sets
##Shopping cart program
##By DA inspired by Bro code

foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit) : ")
    if food.lower() == "q":
        break
    else:
        price = input(f"Enter the price of a {food}: $")
        price = float(price)
        foods.append(food)
        prices.append(price)

print("------ YOUR CART ------")

for food in foods:
    print(food)

for price in prices:
    total = total + price
print()
print("------ TOTAL ------")
print(f"Your total is ${total}")