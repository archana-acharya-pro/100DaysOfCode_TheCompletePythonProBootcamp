# Target is the number up to which we count
def fizz_buzz(target):
    for number in range(1, target + 1):
        # if number % 3 == 0 or number % 5 == 0: # should be an and operator, because we want to check if the number is divisible by both 3 and 5, not just one of them
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        # if number % 3 == 0: # should be an elif, because if the number is divisible by both 3 and 5, it will be caught by the first condition, so we need to check for the condition of being divisible by 3 after checking for the condition of being divisible by both 3 and 5
        elif number % 3 == 0:
            print("Fizz")
        # if number % 5 == 0: # should be an elif, because if the number is divisible by both 3 and 5, it will be caught by the first condition, so we need to check for the condition of being divisible by 5 after checking for the condition of being divisible by both 3 and 5
        elif number % 5 == 0:
            print("Buzz")
        else:
            # print([number]) # should not be a list, because we want to print the number itself, not a list containing the number
            print(number)

fizz_buzz(5)