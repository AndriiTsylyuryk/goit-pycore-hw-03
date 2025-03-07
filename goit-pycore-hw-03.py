from datetime import datetime

def get_days_from_today(date):
    try:
        formatted_date_string=datetime.strptime(date, '%Y-%m-%d')
        now = datetime.today()
        difference =(now.toordinal() - formatted_date_string.toordinal())
        return difference 
    except Exception as e:
        return f'Error: {e}'

print(get_days_from_today('1997-07-31'))

# ////////////////////////////////////////////////////////////
import random

def get_numbers_ticket(min, max, quantity):
    num_list = []

    if min >= 1 and max <= 1000 and quantity <= max:
        while len(num_list) < quantity:
            random_number = random.randint(min,max)
            if random_number not in num_list:
                num_list.append(random_number)  

    num_list.sort()
    return num_list

lottery_numbers = get_numbers_ticket(1, 5, 6)
print("Your numbers:", lottery_numbers)


#/////////////////////////////////////////////////////////////
import re

def normalize_phone(phone_number):
    cleaned_number = re.sub(r'[^\d+]', '', phone_number).strip()
    if cleaned_number.startswith('380'):
        cleaned_number = '+' + cleaned_number
    elif cleaned_number.startswith('0'):
        cleaned_number = '+38' + cleaned_number[1:]
    elif not cleaned_number.startswith('+'):
        cleaned_number = '+38' + cleaned_number
    return cleaned_number

#/////////////////////////////////////////////////////////////

def get_upcoming_birthdays(users):
    dates_list = []

    today = datetime.today().date()

    print(today)

    for user in users:
       formatted_birthday=datetime.strptime(user["birthday"], "%Y.%m.%d").date()
       birthday_this_year = formatted_birthday.replace(year=today.year)
       weekday = birthday_this_year.weekday()
       seven_days = birthday_this_year - today
       print(seven_days)
    #    if birthday_this_year < today:
    #        pass
    #    if seven_days <= 7:
           
        
    #    if weekday != 5 and weekday != 6:
    #        dates_list.append({user['name']})
          


    return dates_list
           
     






users = [
    {"name": "John Doe", "birthday": "1985.03.08"},
    {"name": "Jane Smith", "birthday": "1990.03.12"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)

# [
#     {'name': 'John Doe', 'congratulation_date': '2024.01.23'}, 
#     {'name': 'Jane Smith', 'congratulation_date': '2024.01.29'}
# ]