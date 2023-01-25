# Function that validates data entered by the user
def validate_and_execute(user_input):
    # Checking if the entered data is a number valid
    try:

        user_input_number = int(user_input)
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


