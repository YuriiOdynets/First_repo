#Task №3

import re

def normalize_phone(raw_number):
    cleaned_number = re.sub(r'\D', '', raw_number)
    if not cleaned_number.startswith('+38') and not cleaned_number.startswith('380'):
        cleaned_number = '+38' + cleaned_number
    else:
        cleaned_number = '+' + cleaned_number
    return cleaned_number

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

for raw_number in raw_numbers:
    normalized_number = normalize_phone(raw_number)
    print(normalized_number)

#         OR

#for phone in raw_numbers:
#    cleaned_number=re.sub(r'\D','',phone)
#    if not cleaned_number.startswith('+'):
#        if cleaned_number.startswith('380'):
#            cleaned_number='+'+cleaned_number
#        else:
#            cleaned_number='+38'+cleaned_number
#    print(cleaned_number) 