def odd_or_even(number):
    # if number % 2 = 0: # should be a double equal sign, because we want to compare the value of number % 2 to 0, not assign the value of 0 to number % 2
    if number % 2 == 0:
        return "This is an even number."
    else:
        return "This is an odd number."


odd_or_even(10)