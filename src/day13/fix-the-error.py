# Write your code below this line 👇

age = int(input("How old are you?"))
if age > 18:
# print("You can drive at age {age}.") # Need to indent this line, because it is part of the if statement
#     print("You can drive at age {age}.") # should be an f-string, because we want to include the value of the variable age in the string
    print(f"You can drive at age {age}.")

