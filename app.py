'''
    Write a program that receives a number of days entered by the user and calculate how many minutes this amount of days has.
'''

from subalgorithm_Library import *

print('Days to minutes converter')
days = int(input('Number of days:\n'))

# Function that converts days to hours
hours = converterDaysTime(days)

# Function that converts hours to minutes
minutes = converterHoursToMinutes(hours)
