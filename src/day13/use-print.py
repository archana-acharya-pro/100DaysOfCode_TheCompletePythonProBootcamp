# Write your code below this line 👇

word_per_page = 0
pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: ")) # should be a single equal sign, because we want to assign the value of the input to the variable word_per_page, not compare it to the variable word_per_page
word_per_page = int(input("Number of words per page: "))
total_words = pages * word_per_page

print(f"pages = {pages}")
print(f"words_per_page = {word_per_page}")
print(f"total_words = {total_words}")

print(total_words)


# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
#
# print(f"pages = {pages}")
# print(f"words_per_page = {word_per_page}")
# print(total_words)