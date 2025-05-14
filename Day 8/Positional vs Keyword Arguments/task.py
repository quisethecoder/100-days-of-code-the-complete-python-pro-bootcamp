# Functions with input

# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")

# def greeting(name, location):
#     print(f"Hi {name}, from {location}, welcome!")
#
#
# # greeting("Marquise", "Connecticut")
#
# greeting(location="Connecticut", name="Marquise")

def calculate_love_score(name_one, name_two):
    word = "true"
    word_two = "love"
    true_total = 0
    love_total = 0

    for x in word:
        for a in name_one:
            if x == a:
                true_total += 1
        for b in name_two:
            if x == b:
                true_total += 1

    for letter in word_two:
        for a in name_one:
            if letter == a:
                love_total += 1
        for b in name_two:
            if letter == b:
                love_total += 1

    print(str(true_total) + str(love_total))

calculate_love_score("marquise", "kayon")


# name = "Marquise"
# name_two = "Kayon"
# word = "true"
# word_two = "love"
# true_total = 0
# love_total = 0
#
# for x in word:
#     for a in name:
#         if x == a:
#             true_total += 1
#             print(true_total)
#
#     for b in name_two:
#         if x == b:
#             true_total += 1
#             print(true_total)
#
# for letter in word_two:
#     for a in name:
#         if letter == a:
#             love_total += 1
#             print(love_total)
#     for b in name_two:
#         if letter == b:
#             love_total += 1
#             print(love_total)
#
# print(str(true_total) + str(love_total))





