names = names_string.split(", ")
# The code above converts the input into an array seperating
#each name in the input by a comma and space.
# 🚨 Don't change the code above 👆

import random

num_name = len(names)
choice = random.randint(0, num_name)
spell_name = names[choice]

print(f"{spell_name} is going to buy the meal today!")