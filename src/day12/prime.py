# Write your code below this line 👇

import math


def is_prime(num):
    # Prime numbers must be greater than 1
    if num <= 1:
        return False
    # Check for factors from 2 to sqrt(num)
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False  # Factor found, not prime
    return True  # No factors found, it is prime


# Example usage:
number = 73
if is_prime(number):
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")