<<<<<<< HEAD
print("Welcome to the Pizza Store!!!")
=======
print("Welcome to the Python Pizza Deliveries!")


size = input("What size of pizza do you want? S, M, L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
>>>>>>> 6004fcb53c92e890f95d60117163788a99130731
bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"The price of your pizza is {bill}")
