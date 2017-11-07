def is_leap_year(year):
    # Divisible by four and NOT divisible by 100
    if year % 4 != 0:
        return False
    elif year % 100 !=0:
        return True
    if year % 100 == 0 and year % 400 !=0:
        return False
    elif year % 400 == 0:
        return True





    #if year % 400 == 0:
    #    return True