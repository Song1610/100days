def is_leap_year(year):
    # todo 1 
    if year % 4 == 0:
        
        # todo 2
        if year % 100 == 0:
            
            #todo 3
            if year % 400 == 0:
                return f"{year} is leap year"
            else:
                return f"{year} is not leap year"

            return f"{year} is not leap year"
        else:
            return f"{year} is leap year"

        return f"{year} is leap year"
    else:
        return f"{year} is not leap year"




# Call your function with hard coded values
print(is_leap_year(2100))


