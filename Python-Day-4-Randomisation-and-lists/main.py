import random
import my_module


random_integer = random.randint(1, 10)
print(random_integer)

# print(my_module.pi)

#0.00000 - 0.9999999....
random_float = random.random()
print(random_float)
#0.00000 - 4.9999999....
random_float * 5

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")

states_of_america = ["Delaware", "Pennsylvania"]

states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts",
                     "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina",
                     "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana",
                     "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida",
                     "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia",
                     "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington",
                     "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america)

states_of_america.extend("Gogulan", "Ravichandran")

dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries",
               "Pears", "Tomatoes", "Celery", "Potatoes"]
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]

print(dirty_dozen)

###########Exercise 1 - Heads or Tails##################

# Remember to use the random module
# Hint: Remember to import the random module here at the top of the file. 🎲
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
# 🚨 Don't change the code above 👆 It's only for testing your code.

# Write the rest of your code below this line 👇


random_side = random.randint(0, 1)
if random_side == 1:
    print("Heads")
else:
    print("Tails")

###########Exercise 2 - Banker Roulette##################
import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
# print(names)
length = len(names)
# print (length)

name = names[random.randint(0,length - 1)]

print(f"{name} is going to buy the meal today!")


###########Exercise 3 - Treasure Map##################
