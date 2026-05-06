def calculate_love_score(name1, name2):
    list_of_names = [name1, name2]
    total_true_count = 0
    total_love_count = 0
    for name in list_of_names:
        total_true_count += name.count('t')
        total_true_count += name.count('r')
        total_true_count += name.count('u')
        total_true_count += name.count('e')

        total_love_count += name.count('l')
        total_love_count += name.count('o')
        total_love_count += name.count('v')
        total_love_count += name.count('e')
    print(str(total_true_count) + str(total_love_count))


calculate_love_score("Kanye West".lower(), "Kim Kardashian".lower())