print("Welcome. Check the Leap years available. ")
year = int(input("Which year do you want to check: "))
if year % 4 == 0:
    print("Leap year!")
elif year % 100 != 0:
    print("Not a leap year.")
elif year % 400 != 0:
    print("Not a leap year.")
else:
    print("Leap year!")
