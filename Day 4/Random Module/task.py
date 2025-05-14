import random
# import my_module

# random_integer = random.randint(1,10)
#
#
# print(random_integer + my_module.my_favorite_number)
# print(my_module.my_favorite_number)

# random_number = random.random() * 10
#
# random_float = random.uniform(0,10)
#
# print(random_float)

option1 = "heads"
option2 = "tails"

choose = random.randint(1,2)

if choose == 1:
    print(option1)
else:
    print(option2)
