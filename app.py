'''
    Write a program that receives a number of days entered by the user and calculate how many minutes this amount of days has.
'''

from subalgorithm_Library import *

# Variable
user_input = ''


while user_input != 'exit':
    user_input = input('Enter a number of days to be converted to minutes:\n')

    # Validating the input e running the program
    validate_and_execute(user_input)






