def is_leap_year(year):
    if year % 4 == 0:

        if year % 100 == 0:

            if year % 400 == 0:
                return True
            else:
                return False

            return False
        else:
            return True

        return True
    else:
        return False




# Call your function with hard coded values
print(is_leap_year(2100))


