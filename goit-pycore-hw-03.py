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

