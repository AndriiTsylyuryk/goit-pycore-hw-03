from datetime import datetime, timedelta

def get_days_from_today(date):
    try:
        formatted_date_string=datetime.strptime(date, '%Y-%m-%d')
        now = datetime.today()
        difference =(now.toordinal() - formatted_date_string.toordinal())
        return difference 
    except Exception as e:
        return f'Error: {e}'

print(get_days_from_today('2028-07-31'))

# ////////////////////////////////////////////////////////////
import random

def get_numbers_ticket(min, max, quantity):
    num_list = []

    if min >= 1 and max <= 1000 and quantity <= max:
        while len(num_list) < quantity:
            random_number = random.randint(min,max)
            if random_number not in num_list:
                num_list.append(random_number)
    else: print('Quantity cannot be larger than max') 

    num_list.sort()
    return num_list

lottery_numbers = get_numbers_ticket(1, 10, 11)
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
    
    try:
        dates_list = []
        today = datetime.today().date()
        for user in users:
            formatted_birthday=datetime.strptime(user["birthday"], "%Y.%m.%d").date()
            birthday_this_year = formatted_birthday.replace(year=today.year)
            seven_days = birthday_this_year - today
            if (seven_days.days >= 0 and seven_days.days <= 7) and birthday_this_year.weekday() != 5 and birthday_this_year.weekday() != 6:
                item = {'name': user['name'], 'congrat_dat': birthday_this_year.strftime("%Y.%m.%d")}
                dates_list.append(item)
            elif (seven_days.days >= 0 and seven_days.days <= 7) and birthday_this_year.weekday() == 5: 
                new_date = birthday_this_year + timedelta(days=2)
                item = {'name': user['name'], 'congrat_dat': new_date.strftime("%Y.%m.%d")}
                dates_list.append(item)
            elif (seven_days.days >= 0 and seven_days.days <= 7) and birthday_this_year.weekday() == 6:
                new_date = birthday_this_year + timedelta(days=1)
                item = {'name': user['name'], 'congrat_dat': new_date.strftime("%Y.%m.%d")}
                dates_list.append(item)

        return dates_list  

    except Exception as e:
       return f'Error: {e}'
    
           
     
users = [
    {"name": "John Doe", "birthday": "1985.03.28"},
    {"name": "Jane Smith", "birthday": "1990.03.21"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Congrats list:", upcoming_birthdays)

