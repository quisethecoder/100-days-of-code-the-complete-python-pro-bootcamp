import art

def add(n1, n2):
    return n1 + n2

def subtract(s1, s2):
    return  s1 - s2

def multiply(m1, m2):
    return m1 * m2

def divide(d1, d2):
    return d1 / d2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

# print(operations["*"](4,8))

# Marquise's Way

# continue_calculation = True
#
# calculate_first_num = float(input("Enter the first number into the calculator: "))
# print("+\n-\n*\n/")
# operation_choice = input("Choose an operator: ")
# calculate_second_num = float(input("Enter the second number into the calculator: "))
#
# operation_calculation = operations[operation_choice](calculate_first_num, calculate_second_num)
# current_result = 0
#
# if operation_choice == "+":
#     print(operation_calculation)
#     current_result += operation_calculation
# elif operation_choice == "-":
#     print(operation_calculation)
#     current_result -= operation_calculation
# elif operation_choice == "*":
#     print(operation_calculation)
#     current_result *= operation_calculation
# elif operation_choice == "/":
#     print(operation_calculation)
#     current_result /= operation_calculation
#
#
#
# while continue_calculation:
#     ongoing_calculator = input(f"Type 'y' to continue calculating with {current_result}, type 'n' to start with a new calculation, or type other key to stop: ")
#     if ongoing_calculator == "y":
#         print("+\n-\n*\n/")
#         operation_choice = input("Choose an operator: ")
#         calculate_another_num = float(input("Enter the another number into the calculator: "))
#
#         new_sum = operations[operation_choice](current_result, calculate_another_num)
#
#         if operation_choice == "+":
#             print(new_sum)
#             current_result += calculate_another_num
#         elif operation_choice == "-":
#             print(new_sum)
#             current_result -= calculate_another_num
#         elif operation_choice == "*":
#             print(new_sum)
#             current_result *= calculate_another_num
#         elif operation_choice == "/":
#             print(new_sum)
#             current_result /= calculate_another_num
#     elif ongoing_calculator == "n":
#         calculate_first_num = float(input("Enter the first number into the calculator: "))
#         print("+\n-\n*\n/")
#         operation_choice = input("Choose an operator: ")
#         calculate_second_num = float(input("Enter the second number into the calculator: "))
#
#         operation_calculation = operations[operation_choice](calculate_first_num, calculate_second_num)
#         current_result = 0
#
#         if operation_choice == "+":
#             print(operation_calculation)
#             current_result += operation_calculation
#         elif operation_choice == "-":
#             print(operation_calculation)
#             current_result -= operation_calculation
#         elif operation_choice == "*":
#             print(operation_calculation)
#             current_result *= operation_calculation
#         elif operation_choice == "/":
#             print(operation_calculation)
#             current_result /= operation_calculation
#     else:
#         continue_calculation = False
#         print("Thanks for calculating with us today!")


# Angela Yu's Way

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in operations:
            print(symbol)

        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(
            f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation, or type end to stop: ")

        if choice == "y":
            num1 = answer
        elif choice == "end":
            break
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()



calculator()


