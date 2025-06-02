"""
Problem:
- A Meetup class that takes an integer year and month
- And a day method that takes string DOW and description and gives date

Notes:
- Will use date module here (tried it without and it's too hard for time ROI)
- Can use import datetime and the date function (import datetime as dt)
- We can look at days in 7 week blocks, so 
- "first" = 1-7
- "second" = 8-14
- "third = 15-21
- "fourth = 22-28
- "fifth = 28+, so 29-31
- "last" = last day - 7, so anywheres from 22-28 to 24-31 (so 22-31)
- "teenth" = only looking at the 13th - 19th 

Algorithm:
- Convert the weekday and schedule descriptor to lowercase.
- Calculate the 7 day date range based on the descriptor
- Search the range for the date that occurs on the desired day of the week
    - Can iterate through the days and test if 
    dt.date(year, month, day).weekday() = the numeric conversion of the weekday 
    (i.e. for "teenth" and "Monday" iterate through 13-19 and see if the weekday 
    matches the day)
- Return a date object for the first matching day or a value that indicates 
that a meetup date couldn't be found.
"""

import datetime as dt

class Meetup:
    DAYS_OF_WEEK = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]
    
    def __init__(self, year, month):
        self.year = int(year)
        self.month = int(month)
        # self.is_leap = (self.year % 4 == 0 and self.year % 100 != 0) or (self.year % 400 == 0)
        if self.month == 12:
            self.last_date = (dt.date(self.year + 1, 1, 1) - dt.timedelta(days=1)).day
        else:
            self.last_date = (dt.date(self.year, self.month + 1, 1) - dt.timedelta(days=1)).day
        
    def day(self, day_of_week, description):
        day_of_week = day_of_week.lower()
        description = description.lower()
        
        # days_in_month = {
        #     1: 31,
        #     2: 29 if self.is_leap else 28,
        #     3: 31,
        #     4: 30,
        #     5: 31,
        #     6: 30,
        #     7: 31,
        #     8: 31,
        #     9: 30,
        #     10: 31,
        #     11: 30,
        #     12: 31
        # }
        
        date_windows = {
            'first': 1,
            'second': 8,
            'third': 15,
            'fourth': 22,
            'fifth': 29,
            # 'last': days_in_month[self.month] - 6,
            'last': self.last_date - 6,
            'teenth': 13
        }
        
        # last_date = days_in_month[self.month]
        start_date = date_windows[description]
        end_date = self.last_date if description == 'fifth' else start_date + 6
        index_day = Meetup.DAYS_OF_WEEK.index(day_of_week)
        
        for date in range(start_date, end_date + 1):
            if dt.date(self.year, self.month, date).weekday() == index_day:
                return dt.date(self.year, self.month, date)
                
        return None