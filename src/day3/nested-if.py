# Write your code below this line 👇
from operator import ifloordiv

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry you have to grow taller before you can ride.")

# Nested If - else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    print("Ready to pay for ticket!")
    age = int(input("What is your age? "))
    if age < 12:
        print("Your ticket price for rollercoaster is $5.")
    elif age <= 18:
        print("Your ticket price for rollercoaster is $7.")
    # elif age >= 12 & age <= 18:
    #     print("Your ticket price for rollercoaster is $7.")
    else:
        print("Your ticket price for rollercoaster is $12.")


else:
    print("Sorry you have to grow taller before you can ride.")




print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7.")
    else:
        print("Please pay $12.")
else:
    print("Sorry you have to grow taller before you can ride.")
