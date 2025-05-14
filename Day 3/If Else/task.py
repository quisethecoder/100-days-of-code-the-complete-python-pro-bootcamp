# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))


weight = 85
height = 1.85

bmi = weight / (height ** 2)

# 🚨 Do not modify the values above
# Write your code below 👇

if bmi < 18.5:
    print("underweight")
    print(bmi)
elif bmi >= 18.5 and bmi < 25:
    print("You are normal weight")
    print(bmi)
else:
    print("overweight")
    print(bmi)
