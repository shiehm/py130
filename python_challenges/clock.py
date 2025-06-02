"""
Problem: Create a clock that is independent of date.

Requirements:
- instance "at" method that takes in hour, minute (optional)
    - hour, minute in military time (hours 0-23)
    - returns string time 00:00
    - at(0) is midnight 00:00
- str method also returns string time 00:00
- +/- minutes, returns new clock object
    - if more than a day, just lop the difference
    
Note: I ended up solving it without using an algorithm first. The launch school 
answer is interesting because they convert everything to minutes first before 
calculating the hours. That's smart and saves computation and code space. 
"""

class Clock:
    def __init__(self, hour, minute=0):
        self.hour = int(hour)
        self.minute = int(minute)
    
    @classmethod    
    def at(cls, hour, minute=0):
        return Clock(hour, minute)
    
    def __str__(self):
        return f'{self.hour:02}:{self.minute:02}'
    
    def __add__(self, other):
        if isinstance(other, Clock):
            new_hour = (self.hour + other.hour) % 24
            new_minute = (self.minute + other.minute) % 60
            return Clock(new_hour, new_minute)
        elif isinstance(other, int):
            new_hour = (self.hour + (other // 60)) % 24
            new_minute = (self.minute + (other % 60)) % 60
            return Clock(new_hour, new_minute)
        return NotImplemented
    
    def __sub__(self, other):
        def negative_adjustment(hours, minutes):
            if minutes < 0:
                minutes = 60 + minutes
                hours -= 1
            if hours < 0:
                hours = 24 + hours
            return hours % 24, minutes % 60
        
        if isinstance(other, Clock):
            new_hour = (self.hour - other.hour) % 24
            new_minute = (self.minute - other.minute) % 60
            adj_hour, adj_minute = negative_adjustment(new_hour, new_minute)
            return Clock(adj_hour, adj_minute)
        elif isinstance(other, int):
            hour_delta = (self.hour - (other // 60)) 
            minute_delta = (self.minute - (other % 60)) 
            adj_hour, adj_minute = negative_adjustment(hour_delta, minute_delta)
            return Clock(adj_hour, adj_minute)
        return NotImplemented
        
    def __eq__(self, other):
        if not isinstance(other, Clock):
            return NotImplemented
        return self.hour == other.hour and self.minute == other.minute
        
clock = Clock(10, 15)
print(clock)

print(clock + Clock(1))
print(clock + Clock(14))

clock2 = Clock.at(10, 5)
print(clock2 + clock)

print(clock - 1225)