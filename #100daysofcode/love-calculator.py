print("Welcome to the Love Calculator!")
name1 = input("What is your name: \n")
name2 = input("What is their name: \n")

join_name = name1 + name2
joined_name = join_name.lower()
t = joined_name.count("t")
r = joined_name.count("r")
u = joined_name.count("u")
e = joined_name.count("e")
l = joined_name.count("l")
o = joined_name.count("o")
v = joined_name.count("v")
total_true = str(t + r + u + e)
total_love = str(l + o + v + e)
love_score = int(total_true + total_love)

if (love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 or love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
