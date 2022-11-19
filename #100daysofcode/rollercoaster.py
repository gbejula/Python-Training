print("Welcome to the Roller Coaster Ride!!!")
height = int(input("What is your height: "))
if (height > 120):
    print("You can take the ride")
    age = int(input("What is your age: "))
    if age < 12:
        print("Child ticket is $5")
    elif age <= 18:
        print("Tennager ticket is $7")
    elif age >= 45 and age <= 55:
        print("Your ride is free!")
    else:
        print("Adult ticket is $12")
else:
    print("Sorry you are too young to take the ride.")
