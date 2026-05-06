# Write your code below this line 👇

import random as rnd
random_index = rnd.randint(0, 4)
print(random_index)
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
print(friends)
print(f"way 1: person going to pay: {friends[random_index]}")

# way 2
print(f"way 2: friends going to pay: {rnd.choice(friends)}")