from datetime import datetime

user_input = input('Enter your goal with a deadline separated by colon\n')
input_list = user_input.split(':')

goal = input_list[0]
deadline = input_list[1]

dealine_date = datetime.strptime(deadline,'%d.%m.%Y')
today_date = datetime.today()

# Calculate how many days from now till deadline
time_till = dealine_date - today_date

# Calculate how many hours to till deadline
hours_till = int(time_till.total_seconds() / 60 / 60)
print(f'Time ramainig for your goal: {goal} is {hours_till} hours.')