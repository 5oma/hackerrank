def is_leap(year):
    leap = False
    
    # Write your logic here
    """In the Gregorian calendar three criteria must be taken into account to identify leap years:"""
    # The year can be evenly divided by 4, is a leap year, unless:
    if year % 4 == 0: 
        # The year can be evenly divided by 100, it is NOT a leap year, unless:
        if year % 100 == 0:
        # The year is also evenly divisible by 400. Then it is a leap year.
            if year % 400 == 0:
                return True
            if year % 400 != 0:
                return False
        return True
     



            
    
    print(leap)

year == int(input())
print(is_leap(year))