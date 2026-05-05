# Write your code below this line 👇

from random import randint
dice_images = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6) # should be 0 to 5, because the randint function includes both the start and end values, so if we want to get a number between 0 and 5, we need to use 0 and 5 as the start and end values
dice_num = randint(0, 5)
print(dice_images[dice_num])
