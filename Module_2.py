#num1 = int(input('Please enter your number: '))
#if num1 > 0:
#    print(f'Your number {num1} is positive')
#elif num1<0:
#    print(f'Your number {num1} is negative')
#else:
#    print(f'Your number is 0')
#
#

#money = None
#if money:
#    print(f"You have {money} on your bank account")
#else:
#    print("You have no money and no debts")
#
#num = int(input('Please enter your number: '))
#length = len(str(num))
#if length == 2 and num%2==0:
#    print(f'Ваше число {num}, є парним двозначним числом!')
#else:
#    print(None)

#num = int(input('Please enter your number: '))
#if num%3==0 and num%5==0:
#    print('FizzBuzz')
#elif num%3==0:
#    print('Fizz')
#elif num%5==0:
#    print('Buzz')
#else:
#    print(num)

## Перевіра чи число є парним та двозначним за допомогою оператора and
#num = int(input('Please enter your number: '))
#length = len(str(num))
#if length == 2 and num % 2 == 0:
#    print (f'Digit {num} is dvoznachne parne digit')
#else:
#    print (f'Digit {num} is not dvoznachne parne digit')


##FizzBuzz exercise
#num = int(input('Please enter your digit: '))
#if num % 5 == 0 and num % 25 == 0:
#    print ('FizzBuzz')
#elif num %5 == 0:
#    print ('Fizz')
#elif num %25 ==0:
#    print('Buzz')
#else:
#    print(f'Digit {num} - is not FizzBuzz')

## приклад коду для оператора match
#fruit = input('Please enter fruits name: ')
#match fruit:
#    case 'apple':
#        print ('This is an apple')
#    case 'banana':
#        print ('This is a banana')
#    case _:
#        print(f'{fruit} - this is unknown fruit.')
#
## Приклад використання оператору match для змінних у шаблонах:
#x = int(input('Please enter x: '))
#y = int(input('Please enter y: '))
#point = (x,y)
#
#match point:
#    case (0,0):
#        print('Точка в центрі координат')
#    case (0, y):
#        print(f"Точка лежить на осі Y: y={y}")  
#    case (x, 0):
#        print(f"Точка лежить на осі X: x={x}") 
#    case (x, y):
#        print(f"Точка має координати:  x={x}, y={y}") 
#    case _:
#        print("Це не точка")

##У прикладі літери алфавіту з alphabet виводяться в консоль по черзі, через пробіл.
#alphabet = "abcdefghijklmnopqrstuvwxyz"
#for char in alphabet:
#    print(char, end=" ")

## В прикладі функція проходить по кожному числу з колекції та підносить його до степеня
#odd_numbers = [1, 3, 5, 7, 9]
#for i in odd_numbers:
#    print(i ** 2)

##Цей приклад виводи ь у консоль кількість усіх символів із введеного речення та окремо кількість пробілів у ньому.
#example = input('Please enter your sentance: ')
#
#total_ch = len(example)
#space_count = 0
#
#for ch in example:
#    if ch == ' ':
#        space_count +=1
#print (f'Total character number: {total_ch}')
#print (f'Total space number {space_count}')

##Приклад використання команди break
#a = 0
#while True:
#    print(a)
#    if a >= 20:
#        break
#    a = a + 1

##Приклад використання команди continue
#a=0
#while a<6:
#    a=a+1
#    if not a %2:
#        continue
#    print (a)


##Приклади використання функції range
#for i in range(11):
#    print(i, end = ' ')
#for i in range(5,11):
#    print(i, end = ' ')
#for i in range(0,11,2):
#    print(i, end = ' ')

## Приклад перебору словників по парах 
#dict = {1:'one', 2:'two',3:'three'}
#
## Замість a i b може прийматись будьякі назви. Вони прирівнюються до ключа та значення відповідно у заданому словнику.
#for a,b in dict.items():
#    print (a,b)

#try:
#    value_a = input("Enter value a: ")
#    value_b = input("Enter value b: ")
#
#    value_x = -value_a/value_b
#except TypeError:
#    print("Type Error exception block")
#    try:
#        value_x = -float(value_a)/float(value_b)
#    except ValueError:
#        print("Error!!! could not convert string to float")
#    except ZeroDivisionError:
#        print("Could not divide by zero")
#    else:
#        print(f'Result X equal {round(value_x, 2)}')
#else:
#    print(f'Result X equal {round(value_x, 2)}')
#finally:
#    print('End of calculation')

##Приклад коду що приймає рядок через інпут та перетворює кожен символ у код з подальшим виводом результату у вигляді пар з нового рядка
#string = str(input('Please enter your text: '))
#def string_to_codes(string: str) -> dict:
#    codes = {}
#    for ch in string:
#        if ch not in codes:
#            codes [ch] = ord(ch)
#    return codes
#result = string_to_codes(string)
#for key,value in result.items():
#    print(f'{key}: {value}')


#num = int(input("Enter the integer (0 to 100): "))
#sum = 0
#
#while num > 0:
#    sum=num+sum 
#    num=num-1
#print (sum)

#def format_string(string:str, length:int):
#    if len(string)<length:
#        spaces = ' '*((length-len(string))//2)
#        return print(spaces+string+spaces)
#    else:
#        return print(string)
#format_string('My name', 20)


#def format_string(string:str, length:int):
#    if len(string)<length:
#        spaces = ' '*((length - len(string)) // 2)
#        return spaces+string
#    else:
#        return string
#    
#format_string('Hello', 20)

#def factorial(n):
#    if n < 2:
#        return 1
#    else:
#        return n * factorial(n - 1)
#
#
#def number_of_groups(n, k)->int:
#    total_num = factorial(n)/(factorial(n-k)*factorial(k))
#    return int(total_num)
#
#print(number_of_groups(14,7))


def format_string(string:str, length:int):
    if len(string)<length:
        spaces = ' '*((length - len(string)) // 2)
        return spaces+string
    else:
        return string
    
print(format_string('hello', 20))