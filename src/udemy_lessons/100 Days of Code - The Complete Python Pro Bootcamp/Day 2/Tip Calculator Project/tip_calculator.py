# Write your code below this line 👇

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

tip = bill * tip / 100
bill += tip
print("bill with tip is", bill)
print("tip is", tip)
total_amount = bill / people
print(f'Each person should pay: ${total_amount:.2f}')

total_final_amount = round(total_amount,2)
print(f'Each person should pay: ${total_final_amount}')