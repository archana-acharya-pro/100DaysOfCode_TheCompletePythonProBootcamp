# Write your code below this line 👇

year = int(input("What's your year of birth?"))

if year > 1980 and year < 1994:
    print("You are a millennial.")
# elif year > 1994: # should be elif, because if the year is greater than 1994, it cannot be a millennial, so we need to check for that condition after checking for the millennial condition
elif year >= 1994:
    print("You are a Gen Z.")
