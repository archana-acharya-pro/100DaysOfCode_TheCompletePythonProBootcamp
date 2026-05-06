def life_in_weeks(current_age):
    current_age_in_weeks = current_age * 52
    age_to_live = 90 * 52
    weeks_left = age_to_live - current_age_in_weeks
    print(f"You have {weeks_left} weeks left.")

life_in_weeks(40)