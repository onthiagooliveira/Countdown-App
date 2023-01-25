# Function that validates data entered by the user
def validate_and_execute(user_input):
    # Checking if the entered data is a number valid
    if user_input.isdigit():

        user_input_number = int(user_input)

        # Function that converts days to hours
        hours = converterDaysTime(user_input_number)
        print(hours)

        # Function that converts hours to minutes

    else:
        print('Your entered nis not a valid number.')



# Function that validates and converts days to hours
def converterDaysTime(days):
    if days > 0:
        return f'{days} days are {days * 24} hours.'
    elif days == 0:
        return f'You entered a 0, please enter a valid number'


# Funtion that converts hours to minutes


