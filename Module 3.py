# Модулі datetime та time. Робота з випадковими величинами. Модуль math

#import datetime
#now = datetime.datetime.now()
#print(now)

#import datetime
#
#date_part = datetime.date(2024,4,11)
#time_part = datetime.time(15,23,12)
#
#combined_datetime = datetime.datetime.combine(time_part, date_part)
#
#print(combined_datetime)

#import random
#x = random.randrange(0,100,50)
#print (x)

#import datetime
#
#now=datetime.datetime.now()
#timestamp = datetime.datetime.timestamp(now)
#print(timestamp)

#from datetime import datetime
#
#now = datetime.now()
#
## Форматування дати і часу
#formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
#print(formatted_date) 
#
## Форматування лише дати
#formatted_date_only = now.strftime("%A, %d %B %Y")
#print(formatted_date_only)
#
## Форматування лише часу
#formatted_time_only = now.strftime("%I:%M %p")
#print(formatted_time_only)  
#
## Форматування лише дати
#formatted_date_only = now.strftime("%d.%m.%Y")
#print(formatted_date_only)

#from datetime import datetime
#
#date_string = '2023.03.14'
#try:
#    datetime_object = datetime.strptime(date_string, '%Y.%m.%d')
#    print(datetime_object)
#except:
#    print('Please enter valid date')

#ISO format

#from datetime import datetime
#
#now = datetime.now()
#iso_format = now.isoformat()
#print ( iso_format)
#
#new_now = datetime.fromisoformat(iso_format)
#print(new_now)

##isoclendar() - Повертає кортеж з ISO роком, тижнем та днем
#from datetime import datetime
#
#now = datetime.now()
#
#iso_cal = now.isocalendar()
#print(f'ISO year is: {iso_cal[0]}, ISO week is: {iso_cal[1]}, ISO day is: {iso_cal[2]}')

#from datetime import datetime, timezone
#
#local_now = datetime.now()
#utc_now = datetime.now(timezone.utc)
#
#print(local_now)
#print(utc_now)

#Щоб перетворити UTC час в UTC -5:

#from datetime import datetime, timezone, timedelta
#
#utc_time = datetime.now(timezone.utc)
#print(utc_time)
#eastern_time = utc_time.astimezone(timezone(timedelta(hours = -5)))
#print(eastern_time)

##Поточний час у секундах від 1 січня 1970року
#import time
#current_time=time.time()
#print(current_time)

##Поставити виконання програми на паузу на задану к-ть секунд
#import time
#print ('Hello world!')
#time.sleep(5)
#print ('Hello world after sleep!')

##Перетворення часової мітки у зрозумілий для людини текст. формат ! Якщо нема аргументу - поверне поточний час
#import time 
#current_time=time.time()
#readeble_time=time.ctime(current_time)
#print(readeble_time)

##Приклад використання методу time.perf_counter() для обчислення часу виконання програми:
#import time
#start_time=time.perf_counter()
#for _ in range(1_000_000):
#    pass
#first_part_end= time.perf_counter()
#for _ in range(1_000_000):
#    pass
#end_time= time.perf_counter()
#first_part_execution_time=first_part_end-start_time
#second_part_execution_time=end_time-first_part_end
#
#print(f'Час виконанняя першої частини програми: {first_part_execution_time} секунд.')
#print(f'Час виконанняя другої частини програми: {second_part_execution_time} секунд.')

## Робота з ф-ціями random
#
#import random
#
#fill_percentage = random.random() *100
#print(f'{fill_percentage:.2f}%')

##Перемішування існуючого списку (можливо інших змінних обєктів також?)
#import random
#n=['hello', 'day', 'night', 3, 55]
#print(f'List N before shuffle: {n}')
#random.shuffle(n)
#print(f'List N after shuffle: {n}')


##Вибір одного чи декількохелементу з послідовності, списку чи кортежу. choice-для одного елементу; choices- для декількох елементів. 
#import random
#n=['hello', 'day', 'night', 3, 55]
#print(random.choices(n),2)

##Запобіжник що запрівентить запуск імпортованої функції при її імпорті. Потрібно ставити в кінці своєї функції
##що готується для імпорту.
#
#if __name__ == '__main__':
#
#Отже, рядок if __name__ == '__main__': дозволяє виконувати певний код лише тоді, коли файл запускається безпосередньо, а не 
#імпортується як модуль.

##find і rfind викор для пошуку символів у рядку починаючи з ліва чи з права відповідно:
#str='hello world, this is my test line.'
#print(str.rfind('es'))

##Поділ рядка за певним символом із вказівкою к-ть разів поділу(-1 означатиме поділ без обмежень)
#str='Hello world, this is my test line.'
#result=str.split(' ',3)
#print(result)

##Приклад використання replace
#text='Hello World!'
#new_text=text.replace('orld','')
#print(new_text)


##Задача по перетворенню пошукового запиту на більш зручний формат
##Опреділення змінної із пошуковим запитом
#url_search = "<https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t>"
##Розбиваємо пошуковий запит на дві частини за розділовим знаком ? де _ просто пропуск що забере на себе частину <https://www.google.com/search
##_ використано для ігнорування частини URL до ?
##а query змінна що міститиме другу частину рядка:
#_, query = url_search.split('?')
#print(query)
##Створення порожнього словнику із назвою: obj_query
#obj_query = {}
## Вираз query.split('&') розділяє рядок на окремі параметри за символом & та формує наступний список ['q=Cat+and+dog', 'ie=utf-8', 'oe=utf-8', 'aq=t']
#for el in query.split('&'):
##В середині циклу, кожен параметр el містить ключ та значення, розділені символом =. Спочатку ми розділяємо кожен параметр el на ключ та значення key, value = el.split('=').
#    key, value = el.split('=')
##Вираз obj_query.update... додає пару ключ-значення до словника obj_query. Але ми ще виконуємо value.replace('+', ' ') і замінює символи + на пробіли, оскільки у URL пробіли зазвичай кодуються як +
#    obj_query.update({key: value.replace('+', ' ')})
#print(obj_query)

#Наприклад нам треба розробити програму, яка конвертує рядок, що містить шістнадцяткові числа 
#(в якості окремих символів), у відповідний двійковий код.
#symbols = "0123456789ABCDEF"
#code = [
#        '0000', '0001', '0010', '0011', '0100', '0101', '0110', '0111',
#        '1000', '1001', '1010', '1011', '1100', '1101', '1110', '1111'
#        ]
#
#MAP = {}
#
#for s, c in zip(symbols, code):
#    MAP[ord(s)] = c
#    MAP[ord(s.lower())] = c
#
#result = "34 DF 56 AC".translate(MAP)
#print(result)


#for i in range(8):
#    s = f"int: {i:d};  hex: {i:#x};  oct: {i:#o};  bin: {i:#b}"
#    print(s)


#Приклад форматування вихідного результату по колонках. Результат num буде розміщено у центрі рядку загальною довжиною 10, за ним 
#слідуватиме наступний num з таким самим відступом
#for num in range(12):
#    print(f'{num:^10} {num**2:^10} {num**3:^10}')


#from datetime import datetime
#
#date_string = "2024.01.01"
#
#def string_to_date(date_string):
#    converted_date = datetime.strptime(date_string,'%Y.%m.%d')
#    return converted_date.date()
#converted_date = string_to_date(date_string)
#print(converted_date)
#
#def date_to_string(converted_date):
#    date_string = datetime.strftime(converted_date, '%Y.%m.%d')
#    return date_string

#from datetime import datetime
#
#users = [
#    {"name": "Bill Gates", "birthday": "1955.3.25"},
#    {"name": "Steve Jobs", "birthday": "1955.3.21"},
#    {"name": "Jinny Lee", "birthday": "1956.3.22"},
#    {"name": "John Doe", "birthday": "1985.01.23"},
#    {"name": "Jane Smith", "birthday": "1990.01.27"}
#]
#
#def string_to_date(users):
#    return datetime.strptime(users, "%Y.%m.%d").date()
#for bd in users:
#    bd['birthday'] = string_to_date(bd['birthday'])
#print(users)
#
#
#def prepare_user_list(users):
#    prepared_users = []
#    for user in users:
#        name = user["name"]
#        birthday_str = user["birthday"]
#        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()
#        prepared_user = {"name": name, "birthday": birthday_date}
#        prepared_users.append(prepared_user)
#    return prepared_users

#!!!from datetime import datetime, timedelta
#!!!
#!!!users = [
#!!!    {"name": "Bill Gates", "birthday": "1955.3.25"},
#!!!    {"name": "Steve Jobs", "birthday": "1955.3.21"},
#!!!    {"name": "Jinny Lee", "birthday": "1956.3.22"},
#!!!    {"name": "John Doe", "birthday": "1985.01.23"},
#!!!    {"name": "Jane Smith", "birthday": "1990.01.27"}
#!!!]
#!!!
#!!!def string_to_date(users):
#!!!    return datetime.strptime(users, "%Y.%m.%d").date()
#!!!for bd in users:
#!!!    bd['birthday'] = string_to_date(bd['birthday'])
#!!!#print(users)
#!!!
#!!!def prepare_user_list(users):
#!!!    prepared_users = []
#!!!    for user in users:
#!!!        name = user["name"]
#!!!        birthday_str = user["birthday"]
#!!!        birthday_date = datetime.strptime(birthday_str, "%Y.%m.%d").date()
#!!!        prepared_user = {"name": name, "birthday": birthday_date}
#!!!        prepared_users.append(prepared_user)
#!!!    return prepared_users
#!!!        
#!!!def find_next_weekday(start_date, weekday=0):
#!!!    days_ahead = (weekday - start_date.weekday() + 7)
#!!!    next_weekday_date = start_date + timedelta(days_ahead)
#!!!    return next_weekday_date
 
#def find_next_weekday(prepared_users, weekday=0):
#    next_weekday_birthdays=[]
#    for user in prepared_users:
#        name = user["name"]
#        birthday_date = user["birthday"]
#        current_weekday=birthday_date.weekday()
#        days_until_target_weekday = (weekday - current_weekday+7)%7
#        next_weekday_date=birthday_date+timedelta(days=days_until_target_weekday)
#        next_weekday_birthdays.append({'name':name,'next_birthday':next_weekday_date})
#    return next_weekday_birthdays
#print(find_next_weekday(users))

#def find_next_weekday(prepared_users, weekday=0):
    #next_weekday_dates=[]
    #for user in prepared_users:
    #    birthday_date = user["birthday"]
    #    days_until_target_weekday = (weekday - birthday_date.weekday() + 7) % 7
    #    next_weekday_date = birthday_date + timedelta(days=days_until_target_weekday)
    #    if next_weekday_date.weekday() >= 5:
    #        next_weekday_date += timedelta(days=(7 - next_weekday_date.weekday()) + (2 if next_weekday_date.weekday() == 5 else 1))
    #    next_weekday_dates.append(next_weekday_date)
    
    #return next_weekday_dates
#    days_until_target_weekday = (weekday - prepared_users.weekday() + 7) % 7
#    next_weekday_date = prepared_users + timedelta(days=days_until_target_weekday)
#    if next_weekday_date.weekday() >= 5:
#        next_weekday_date += timedelta(days=(7 - next_weekday_date.weekday()) + (2 if next_weekday_date.weekday() == 5 else 1))
#    
#    return next_weekday_date    
#print(find_next_weekday(users))


#from datetime import datetime, date
#
#
#def string_to_date(date_string):
#    return datetime.strptime(date_string, "%Y.%m.%d").date()
#
#
#def date_to_string(date):
#    return date.strftime("%Y.%m.%d")
#
#
#def prepare_user_list(user_data):
#    prepared_list = []
#    for user in user_data:
#        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
#    return prepared_list
#
#
#def get_upcoming_birthdays(users, days=7):
#    upcoming_birthdays = []
#    today=date.today()
#    for user in users:
#        birthday=user['birthday']
#        next_birthday_year=today.year if birthday.month >= today.month and birthday.day >= today.day else today.year +1
#        next_birthday = date(next_birthday_year, birthday.month, birthday.day)
#        days_until_birthday = (next_birthday-today).days
#        if 0 < int(days_until_birthday) <= days:
#            congratulation_date = next_birthday.strftime("%Y.%m.%d")
#            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})
#    return upcoming_birthdays
#        
#users = [
#    {"name": "Sarah Lee", "birthday": "1957.03.30"},
#    {"name": "John Doe", "birthday": "1985.03.28"},
#    {"name": "Jane Smith", "birthday": "1990.03.27"},
#    {"name": "John Doe", "birthday": "1985.01.23"},
#]
#
#prepared_users = prepare_user_list(users)
#print(get_upcoming_birthdays(prepared_users, 7))


from datetime import datetime, date


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()
    
    for user in users:
        birthday = user["birthday"].replace(year=today.year)
        days_until_birthday = (birthday - today).days
        
        if 0 <= days_until_birthday <= days:
            congratulation_date = date_to_string(birthday)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date})
    
    return upcoming_birthdays

users = [
    {"name": "Sarah Lee", "birthday": "1957.03.30"},
    {"name": "John Doe", "birthday": "1985.03.28"},
    {"name": "Jane Smith", "birthday": "1990.03.27"},
    {"name": "John Doe", "birthday": "1985.01.23"},
]

prepared_users = prepare_user_list(users)
print(get_upcoming_birthdays(prepared_users, 7))


def adjust_for_weekend(birthday):
    if birthday.weekday() >=5:
        next_monday=find_next_weekday(birthday,0)
        return next_monday
    else:    
        return birthday
    
#    def get_upcoming_birthdays(users, days=7):
#    upcoming_birthdays = []
#    today = date.today()
#
#    for user in users:
#        birthday_this_year = user["birthday"].replace(year=today.year)
#
#        # Перевірка, чи не буде день народження вже наступного року
#        if birthday_this_year < today:
#            birthday_this_year = user["birthday"].replace(year=today.year + 1)
#
#        # Перенесення дати привітання на наступний робочий день, якщо день народження припадає на вихідний
#        birthday_this_year = adjust_for_weekend(birthday_this_year)
#
#        # Перевірка, чи день народження в межах вказаного періоду days
#        if 0 <= (birthday_this_year - today).days <= days:
#            congratulation_date_str = date_to_string(birthday_this_year)
#            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
#
#    return upcoming_birthdays


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year<today:
            birthday_this_year = user['birthday'].replace(year=today.year +1)
        birthday_this_year = adjust_for_weekend(birthday_this_year)

        if 0 <= (birthday_this_year - today).days <= days:
            congratulation_date_str=date_to_string(birthday_this_year)
            upcoming_birthday.append({'name':user['name'],'cngratulation_date':congratulation_date_str})
    return upcoming_birthdays


from datetime import datetime, date, timedelta


def string_to_date(date_string):
    return datetime.strptime(date_string, "%Y.%m.%d").date()


def date_to_string(date):
    return date.strftime("%Y.%m.%d")


def prepare_user_list(user_data):
    prepared_list = []
    for user in user_data:
        prepared_list.append({"name": user["name"], "birthday": string_to_date(user["birthday"])})
    return prepared_list


def find_next_weekday(start_date, weekday):
    days_ahead = weekday - start_date.weekday()
    if days_ahead <= 0:
        days_ahead += 7
    return start_date + timedelta(days=days_ahead)


def adjust_for_weekend(birthday):
    if birthday.weekday() >= 5:
        return find_next_weekday(birthday, 0)
    return birthday


def get_upcoming_birthdays(users, days=7):
    upcoming_birthdays = []
    today = date.today()

    for user in users:
        birthday_this_year = user["birthday"].replace(year=today.year)
        if birthday_this_year<today:
            birthday_this_year = user['birthday'].replace(year=today.year +1)
        birthday_this_year = adjust_for_weekend(birthday_this_year)

        """
        Додайте на цьому місці перевірку, чи не буде 
        припадати день народження вже наступного року.
        """
        
            

        if 0 <= (birthday_this_year - today).days <= days:
            """ 
            Додайте перенесення дати привітання на наступний робочий день,
            якщо день народження припадає на вихідний. 
            """
            

            congratulation_date_str = date_to_string(birthday_this_year)
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})
    return upcoming_birthdays