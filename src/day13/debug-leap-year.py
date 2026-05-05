def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            # if year % 4000 == 0: # should be 400, because a year that is divisible by 400 is a leap year, but a year that is divisible by 4000 is not a leap year, so we need to check for that condition after checking for the condition of being divisible by 100
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

is_leap(2020)