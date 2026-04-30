
# Write your code below this line 👇

#len() doesn't work with int and number
#len(12345)
len("12345")

# type() displays type of the variable
print(type("12345"))
print(type(12345))
print(type(12345.45))
print(type(1234567890456789))
print(type(123_456_8904_567_89))
print(type("Hello World"))
print(type(True))
print(type(False))

# type conversion

print(int("123")+int("456"))
# print(int("abc")*int("456")) # will reurn error invalid literal for int() with base 10: 'abc'

# print("Number of letters in your name: " + len(input("Enter your name"))) # Error can only concatenate str (not "int") to str
print("Number of letters in your name: " + str(len(input("Enter your name: "))))

user_name = input("Enter your name: ") # str
print(type(user_name))

length = len(user_name) # int
print(type(length))

print("Number of letters in your name: " + str(length)) # str

# TypeError
# len(123)

# No TypeError
len("Hello")

# Type Checking
print(type("abc"))
print(type(123))
print(type(3.14))
print(type(True))

# Type Conversion
str()
int()
float()
bool()

name_of_the_user = input("Enter your name")
length_of_name = len(name_of_the_user)

print(type("Number of letters in your name: "))  # str
print(type(length_of_name))  # int

print("Number of letters in your name: " + str(length_of_name))


