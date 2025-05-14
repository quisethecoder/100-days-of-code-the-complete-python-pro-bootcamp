programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The act of doing something repetitive",
}


print(programming_dictionary["Function"])

programming_dictionary["Global"] = "Means it can be used outside of function as well as in"

print(programming_dictionary)

# editing a dictionary
programming_dictionary["Bug"] = "A moth in computer"
print(programming_dictionary["Bug"])

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])