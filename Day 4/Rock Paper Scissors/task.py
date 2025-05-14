import random
from random import choice

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]
random_option = random.choice(options)


computer = random_option
player_one = input("Pick a choice... 0 for rock, 1 paper or 2 for scissors?: ").lower()

print("computer chose: " + computer)


if player_one == "0":
    player_one = options[0]
    print("you chose: " + rock)
    if computer == rock:
        print("It's a tie!")
    elif computer == paper:
        print("computer wins")
    elif computer == scissors:
        print("player 1 wins")
    else:
        print("That isn't a option")
elif player_one == "1":
    player_one = options[1]
    print("you chose: " + paper)
    if computer == rock:
        print("player 1 wins")
    elif computer == paper:
        print("It's a tie!")
    elif computer == scissors:
        print("computer wins!")
    else:
        print("That's not an option")
elif player_one == "2":
    player_one = options[2]
    print("you chose: " + scissors)
    if computer == scissors:
        print("It's a tie!")
    elif computer == rock:
        print("computer wins")
    elif computer == paper:
        print("player 1 wins")
    else:
        print("That's not an option")
else:
    print("That's not a option")















