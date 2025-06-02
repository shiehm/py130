"""
Problem:
- A Meetup class that takes an integer year and month
- And a day method that takes string DOW and description and gives date

Requirements:
- 

Notes:
- We can try to solve this using relative distance from a date that we know the 
day of (June 1st, 2025 was a Sunday). 
- We can actually construct a helper function that gives the first day of the 
month if you just plug in the year and month 

Helper function for determining starting day of month:
The goal of this function is to determine how many days % 7 away from the 
anchor day of Wednesday January 1st, 2025 the 1st of the month, year in question is. 
It should function whether the date is in the future or the past + / -, we can
calculate the number of times each month is "passed" relative to the anchor days.
- Set anchor variables for the anchor_month and anchor_year
- Calculate how many months difference the anchor date is from the Meetup date
- Take the number of months difference // 12 * 29 (sign will be in the months)
- Take the number of months % 12 will tell you how many months from Jan to go 

Helper function for determining number of leap years:
- Take the number 

Algorithm: 

"""

class Meetup:
    DAYS_IN_MONTH = {
        'January': 31,
        'February': 28,
        'March': 31,
        'April': 30,
        'May': 31,
        'June': 30,
        'July': 31,
        'August': 31,
        'September': 30,
        'October': 31,
        'November': 30,
        'December': 31
    }
    
    DAYS_OF_WEEK = [
        'Sunday',
        'Monday',
        'Tuesday',
        'Wednesday',
        'Thursday',
        'Friday',
        'Saturday'
    ]
    
    def __int__(self, year, month):
        self.year = int(year)
        self.month = int(month)
    
    def calc_first_day(self, year, month):
        anchor_year = 2025 
        anchor_month = 1
        anchor_first_day = 'Wednesday'
        
        year_delta = year - anchor_year
        month_delta = month - anchor_month
        total_months_exleap = (year_delta * 12) + month_delta
        
        def calc_leap_days(year, month):
            leap_days = 0
            for current_year in range(year, anchor_year, step):
                
    
    def day(self, day_of_week, description):
        
        
        return date