# Write your code below this line 👇

# bmi = 84 / 1.65 ** 2  # bmi is equal to the person's weight divided by the person's height squared.

weight = 85
height = 1.85
bmi = weight / (height ** 2)
print(bmi)

# 🚨 Do not modify the values above
# Write your code below

if bmi < 18.5:
    print("You are underweight")
elif bmi >= 18.5 and bmi < 25:
        print("You are normal")
else:
    print("You are obese")