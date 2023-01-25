'''
    Write a program that receives a number of days entered by the user and calculate how many minutes this amount of days has.
'''

from subalgorithm_Library import *

print('Days to minutes converter')
user_input = input('Number of days:\n')

#Checking if the entered data is a number valid
if user_input.isdigit():
    user_input_number = int(user_input)

    # Function that converts days to hours
    hours = converterDaysTime(user_input_number)
    print(hours)

    # Function that converts hours to minutes



