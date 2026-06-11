def is_year_leap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    # if statement
        # ...
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    res  = days[month - 1]
    if month == 2 and is_year_leap(year):
        res = 29
    return res

def day_of_year(year, month, day):
    #
    # Write your new code here.
    #
    ref_date="1/1/2000"
    ref_day= "Saturday"
    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    

print(day_of_year(2000, 12, 31))
