import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
# print(len(letters))

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))


password = []

#first I want to work on getting random letters from the list array
# Next get the amount of random letters that is given by the user input

user_range = range(nr_letters)
user_symbol_range = range(nr_symbols)
user_number_range = range(nr_numbers)

# random_letters = random.choice(letters)
# random_numbers = random.choice(numbers)
# random_symbols = random.choice(symbols)



for x in user_range:
    password.append(random.choice(letters))

for x in user_symbol_range:
    password.append(random.choice(symbols))

for x in user_number_range:
    password.append(random.choice(numbers))

random.shuffle(password)

message = "Your password is: "

print(message, *password, sep='')
print(len(password))


generation = ""

for char in user_range:
    generation = generation + random.choice(letters)

for char in user_symbol_range:
    generation = generation + random.choice(symbols)

for char in user_number_range:
    generation = generation + random.choice(numbers)


get = list(generation)
random.shuffle(get)
result = "".join(get)
print(message, result)





# print(random_letters,random_numbers, random_symbols)




















