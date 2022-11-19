import random
names_string = input("Give everyone's name separated by a comma\n")
names = names_string.split(",")
name_length = (len(names))
rand_num = random.randint(0, name_length -1 )
person_to_pay = names[rand_num]
print(person_to_pay + ' will pay for the meals and drink today.')