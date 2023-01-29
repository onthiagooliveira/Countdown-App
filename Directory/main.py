"""
    Write a program that takes a user-entered number of days  and calculates progress toward a user-defined goal.
"""


# subalgorithm_Library

# Function that validates and converts days to hours and minutes
def convert_days_to_hours(num_of_days, conversion_unit):
    if conversion_unit == 'hours':
        return f'{num_of_days} days are {num_of_days * 24} hours.'

    elif conversion_unit == 'minutes':
        return f'{num_of_days} days are {num_of_days * 24 * 60 } minutes.'

    else:
        return 'Unsupported unit.'


# Function that validates a number entered by the user
def validate_and_execute():
    # Checking if the entered data is a number valid
    try:
        user_input_number = int(days_and_unit_dictionary["days"])
        if user_input_number > 0:
            calculated_value = convert_days_to_hours(user_input_number, days_and_unit_dictionary["unit"])
            print(calculated_value)
        elif user_input_number == 0:
            print('You input a 0, please enter a positive number')
        else:
            print('It is not possible to convert, you entered a negative number.')
    except ValueError:
        print('Your input is not a valid number.')




# Running Aplication

# Variables
user_input = ""

while user_input != 'exit':
    user_input = input('Enter a number of days and conversion unit:\n')
    days_and_unit = user_input.split(":")
    print(days_and_unit)
    days_and_unit_dictionary = {"days": days_and_unit[0], "unit": days_and_unit[1]}
    print(days_and_unit_dictionary)
    print(type(days_and_unit_dictionary))
    validate_and_execute()

