"""
    Write a program that takes a user-entered number of days  and calculates progress toward a user-defined goal.
"""

# subalgorithm_Library

# Function that validates a number entered by the user
def validate_and_execute():
    # Checking if the entered data is a number valid
    try:
        user_input_number = int(num_of_days_element)
        if user_input_number > 0:
            calculated_value = convert_days_to_hours(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print('You entered a 0, please enter a positive number')
        else:
            print('It is not possible to convert, you entered a negative number.')
    except ValueError:
        print('Your entered is not a valid number.')


# Function that validates and converts days to hours
def convert_days_to_hours(days):
    return f'{days} days are {days * 24} hours.'


# Funtion that converts hours to minutes
def convert_hours_to_minutes(hours):
    return f'{hours} hours are {hours * 60} minutes.'







# Running Aplication

# Variables
user_input = ''



while user_input != 'exit':
    user_input = input('Enter a number of days to be converted to minutes:\n')

    for num_of_days_element in user_input.split(","):
        # Validating the input e running the program
        validate_and_execute()
