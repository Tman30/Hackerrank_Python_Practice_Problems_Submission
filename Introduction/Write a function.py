def is_leap(year):
    leap = False
    
    if year%4 == 0:
        if not (year%100 == 0 and year%400 != 0):
            leap = True
    
    return leap