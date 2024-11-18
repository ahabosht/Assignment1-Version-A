#!/usr/bin/env python3

'''
OPS445 Assignment 1 - Fall 2024
Program: assignment1.py 
Author: "Ahmad Habosht"
Seneca User: "ahabosht"
The python code in this file (assignment1.py) is original work written by
"Ahmad Habosht". No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading. I understand
that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''

import sys

def day_of_week(year: int, month: int, date: int) -> str:
    "Based on the algorithm by Tomohiko Sakamoto"
    days = ['sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat'] 
    offset = {1:0, 2:3, 3:2, 4:5, 5:0, 6:3, 7:5, 8:1, 9:4, 10:6, 11:2, 12:4}
    if month < 3:
        year -= 1
    num = (year + year//4 - year//100 + year//400 + offset[month] + date) % 7
    return days[num]

def mon_max(month, year):
    "returns the maximum day for a given month. Includes leap year check"
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12: 
        return 31
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 30
    elif month == 2:
        if leap_year(year):
            return 29
        else:
            return 28
    else:
        raise ValueError("Invalid month value") #raise an error if the month is invalid

def after(date: str) -> str:
    '''
    after() -> date for next day in YYYY-MM-DD string format

    Return the date for the next day of the given date in YYYY-MM-DD format.
    This function takes care of the number of days in February for leap year.
    This fucntion has been tested to work for year after 1582
    '''
    str_year, str_month, str_day = date.split('-')
    year = int(str_year)
    month = int(str_month)
    day = int(str_day)
    tmp_day = day + 1  # next day

    if tmp_day > mon_max(month, year):
        to_day = tmp_day % mon_max(month, year)  # if tmp_day > this month's max, reset to 1 
        tmp_month = month + 1
    else:
        to_day = tmp_day
        tmp_month = month + 0

    if tmp_month > 12:
        to_month = 1
        year = year + 1
    else:
        to_month = tmp_month + 0

    next_date = f"{year}-{to_month:02}-{to_day:02}"

    return next_date

def usage():
    "Print a usage message to the user"
    print("Usage: assignment1.py YYYY-MM-DD YYYY-MM-DD") #print the way the date format should be.
    sys.exit(1) #exit if the arguments are wrong

def leap_year(year):
    "return True if the year is a leap year"
    if year % 4 == 0:
        if year % 100 != 0 or year % 400 == 0:
            return True
    return False


def valid_date(date):
    "check validity of date and return True if valid"
    try:
        parts = date.split("-") #split the date into separate parts
        if len(parts) != 3: #check if the format is correct
            return False

        year, month, day = parts 

        year = int(year)
        month = int(month)
        day = int(day)

        if len(str(year)) != 4: #check that the year is 4 digits
            return False

        if month < 1 or month > 12:
            return False

        max_days = mon_max(month, year) #check the max days in this month
        if day < 1 or day > max_days:
            return False

        return True

    except ValueError:
        return False

def day_count(start_date, stop_date):
    "Loops through range of dates, and returns number of weekend days"
    start, stop = sorted([start_date, stop_date]) #Sort start and stop in the right order.
    weekend_days = 0 #weekend_days counter start from Zero

    while start <= stop:
        year, month, day = map(int, start.split('-')) #split the date and convert each part into integer.
        if day_of_week(year, month, day) == 'sat' or day_of_week(year, month, day) == 'sun':
            weekend_days += 1 #increment by 1
        start = after(start) #call the after() function to get the next day

    return weekend_days

if __name__ == "__main__": #main block
    if len(sys.argv) != 3: #check if the right number of arguments are provided
        usage() #call usage() function to show usage message if the provided arguments are wrong

    start_date = sys.argv[1] #obtain start date from arguments
    stop_date = sys.argv[2] #obtain stop date from arguments

    if valid_date(start_date) == False or valid_date(stop_date) == False: #check if the dates are valid
        usage() #if not, call usage() function to show usage message

    weekend_days = day_count(start_date, stop_date) #calculate the number of weekend days
    start, stop = sorted([start_date, stop_date]) #sort the dates in order
    print(f"The period between {start} and {stop} includes {weekend_days} weekend days.") #print the result
