# Write your code below this line 👇

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        price = 5
        print("Child ticket is $5.")
    elif age <= 18:
        price = 7
        print("Youth ticket is $7.")
    else:
        price = 12
        print("Adult ticket is $12.")
    want_photo = (input("Would you like to see a photo? Type y for Yes, n for No. ")).lower()
    if want_photo == 'y':
        price += 3
    print(f"Your final price is ${price}")
else:
    print("Sorry you have to grow taller before you can ride.")


