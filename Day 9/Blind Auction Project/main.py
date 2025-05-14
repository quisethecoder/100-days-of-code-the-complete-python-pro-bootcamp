# TODO-1: Ask the user for input
# Ask for name
# Add for price
# TODO-2: Save data into dictionary {name: price}
# Add name and price into dictionary as key: value pair
# TODO-3: Whether if new bids need to be added
# Ask if there are any other bids if yes loop back to asking for name
# if no print the highest bidder as the winner
# TODO-4: Compare bids in dictionary
import art

print(art.logo)

# name = input("what is you name?: ")
# price = input("What is your bid price?: ")
#
#
# bids = {
#     name: price
# }
#
#
# bid_again = input("Is there another bidder [yes/no]?: ")
# if bid_again == "no":
#     print(f"Congrats {name}! you bid {bids[name]}, and that was the only bid so you won!")
# else:
#     print("\n" * 20)
#
# while bid_again == "yes":
#     name = input("what is you name?: ")
#     price = input("What is your bid price?: ")
#
#     bids[name] = price
#
#     bid_again = input("Is there another bidder [yes/no]?: ")
#     print("\n" * 20)
#
#     if bid_again == "no":
#         highest_bid = max(bids, key=bids.get)
#         bid_value = max(bids.values())
#         print(f"congratulations {highest_bid}! You bid the highest amount {bid_value}.")
#         break


def highest_bid(biddington):
    bidder_name = ""
    highest_value = 0

    for x in biddington:
        if int(bids[x]) > highest_value:
            bidder_name = x
            highest_value = int(bids[x])
    print(f"congrats {bidder_name}! You won with the highest bid ${highest_value}")


bids = {}
continue_bid = True

while continue_bid:
    name = input("what is you name?: ")
    price = input("What is your bid price?: ")

    bids[name] = price

    bid_again = input("Is there another bidder [yes/no]?: ").lower()

    if bid_again == "no":
        continue_bid = False
        highest_bid(biddington=bids)
    else:
        print("\n" * 20)


