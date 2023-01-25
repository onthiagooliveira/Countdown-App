
# Function that validates and converts days to hours
def converterDaysTime(days):
    if days > 0:
        return f'{days} days are {days * 24} hours.'
    elif days == 0:
        return f'You entered a 0, please enter a valid number'
    else:
        return f'Invalid value. You entered a negative value.'



# Funtion that converts hours to minutes


