# Write your code below this line 👇

print(range(1,10))
sum = 0
for number in range(1,10):
    print(number)
    sum += number
print(f"sum in the range 1:10 is: {sum})")

sum = 0
for number in range(1, 10, 2):
    print(number)
    sum += number
print(f"sum in the range 1:10 with step of 2 is: {sum})")

sum = 0
for number in range(1, 101):
    sum += number
print(f"sum in the range 1:100 is: {sum})")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for letter in range(0, 5):
    print(letters[letter])
    print("Your password is: ", letter)