print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

bill_tip_amount = tip / 100 * bill

bill_plus_tip = bill + bill_tip_amount

total = bill_plus_tip / people

final = round(total, 2)



print(f"each person should pay: {total}")


