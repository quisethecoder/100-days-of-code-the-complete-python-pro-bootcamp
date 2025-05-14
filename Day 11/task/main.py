import random


from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


play_game = True


while play_game:
    begin_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")

    player_one_cards = []
    computer_cards = []

    if begin_game == "y":
        print("\n" * 20)
        print(logo)
        player_card1 = random.choice(cards)
        player_card2 = random.choice(cards)
        player_one_cards.append(player_card1)
        player_one_cards.append(player_card2)
        player1_card_total = sum(player_one_cards)

        print(f"Your cards: {player_one_cards}, current score: {player1_card_total}")
        computer_card1 = random.choice(cards)
        computer_cards.append(computer_card1)
        computer_card_total = sum(computer_cards)
        print(f"Computer's first card: {computer_card_total}")

        hit_or_stand = input("Type 'y' to get another card, type 'n' to pass: ")
        continue_hit = True

        while continue_hit:
            if hit_or_stand == "y" and player1_card_total < 21:
                player_additional_card = random.choice(cards)
                player_one_cards.append(player_additional_card)
                player1_card_total = sum(player_one_cards)
            elif hit_or_stand == "y" and player1_card_total > 21:
                continue_hit = False
                print(f"Your final hand {player_one_cards}, final score: {player1_card_total}")
                print("You went over 21, you lose :(")






