print("Welcome to the Python Pizza Deliveries!")


size = input("What size of pizza do you want? S, M, L: ")
# add_pepperoni = input("Do you want pepperoni? Y or N: ")
# extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0

if (size == "S"):
    bill += 15
    print(f"The price of your pizza is: {bill}")
elif (size == "M"):
    bill += 20
    print(f"The price of your pizza is: {bill}")
elif (size == "L"):
    bill += 25
    print(f"The price of your pizza is: {bill}")
else:
    print("Sorry, you selected the wrong input.")
