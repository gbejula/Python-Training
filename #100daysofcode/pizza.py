print("Welcome to the Pizza Store!!!")
#small pizza
S = 15

#medium pizza
M = 20

#large pizza
L = 25
bill = 0

size = input("What size of pizza do you want: ")

if (size == "S"):
    bill += 15
elif (size == "M"):
    bill += 20
elif (size == "L"):
    bill += 25
    print(f"The price of your pizza is: {bill}")
else:
    print("Sorry, you selected the wrong input.")