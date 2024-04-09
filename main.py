#create list collection
#my_list = ['a','b','c',33,2,2,2,2]
#print (my_list)

#extend one list with another
#my_list2 = [1,2,3]
#my_list.extend(my_list2)
#print (my_list2)
#print (my_list)

#add new list colection element via value
#my_list.append('new')
#print (my_list[0])

#remove list collection element via value
#my_list.remove('a')
#print (my_list[-3])

#return element by the index and remove it from original list collection
#f1 = my_list.pop(1)
#print (my_list,f1)

#list elment change via index
#print(my_list)
#my_list[0] = -22
#print(my_list)

#insert new element on specific index place
#my_list.insert(0, 5)
#print (my_list)

#clear entire list collection 
#my_list.clear()
#print (my_list)

#return index number of first element entry in the list
#print(my_list.index(33))

#count number of times specific element present in the list
#if element is not present in the list, method will return 0 as result
#print(my_list.count(2))

#find number of elements in the list
#print(len(my_list))

#sort collection by growth
#num_list = [4,8,2.53,43.2,2]
#print(num_list)
#num_list.sort()
#print (num_list)

#sort collection by decline
#num_list = [4,8,2,43,2]
#print(num_list)
#num_list.sort(reverse=True)
#print (num_list)

#sort collection with str elements by key value
#list = ['a','aa','aaaaaa','aaa']
#print (list)
#list.sort(key=len)
#print (list)

#create new sorted list
#list = [100,8,6,10]
#print (list)
#sorted_list = sorted(list)
#print (sorted_list)

#create new sorted list desc
#list = [100,8,6,10]
#print (list)
#sorted_list = sorted(list, reverse=True)
#print (sorted_list)

#copy existing list
#num = [1,2,3]
#num_copy = num.copy()
#print (num)
#print (num_copy)

#reverse the order of elements
#num = [1,2,3]
#print (num)
#num.reverse()
#print (num)

#dicktionary creation and value return by the name
#dict={"name":"Yurii","course":"GoIT","x":"habsdbu"}
#print (dict["course"])

#dict={1:'a',2:'b',3:'c'}
#print(dict)
#print(dict[2])

#change and append dict with new values
#dict={1:'a',2:'b',3:'c'}
#print(dict)
#dict[1]='Hello World!'
#dict[4]='d'
#print (dict[1])
#print(dict)

#key pair deletion
#dict={1:'a',2:'b',3:'c'}
#print(dict)
#del dict[1]
#print(dict)

#check if key is present in dictionary
#dict={1:'a',2:'b',3:'c'}
#print(1 in dict)
#del dict[1]
#print(1 in dict)

#remove key-value pair from the dict and return value as argument x
#dict={1:'a',2:'b',3:'c'}
#x = dict.pop(1)
#print(dict, x)
#y = dict.pop(2)
#print(dict, x, y)


#update existing dictionary by the new dictionary (old keys will be updated with new values, and new keys will be created)
#dict={1:'a',2:'b',3:'c'}
#print(dict)
#dict.update({3:'d', 4:'e'})
#print(dict)

#clear dictionary
#dict={1:'a', 2:'b'}
#print (dict)
#dict.clear()
#print(dict)

#create a copy of existing dictionary without deleting it
#dict={1:'a', 2:'b'}
#copy_dict=dict.copy()
#print (copy_dict)


#safe return of value by the key (if key will not be fond in dict, it will return None)
#dict={1:'a', 2:'b'}
#x = dict.get(1)
#y = dict.get(3)
#print (x, y)
#print (dict)

#[] can be used in stead of .get Problem is that if key will not be found, it will return KeyError error message.

#create set 
#a = {1,1,2,2,3,3}
#print (a)


#remove dublicates from the list collection by transforming it to Set and back
#test_collection = [1,2,3,4,4,3,2,5,6,10]
#test_collection_set = set(test_collection)
#print(test_collection)
#test_collection=list(test_collection_set)
#print(test_collection)


#add new element in to set
#x = {1,2,3}
#x.add(4)
#print(x)


#remove element from set. Calls exception error in case if element not found (KeyError)
#x = {1,2,3}
#x.remove(2)
#print(x)
##x.remove(4)
#print(x)


#remove elem from the set without exception error in case if elem not found in set
#x = {1,2,3}
#x.discard(2)
#print(x)
#x.discard(4)
#print(x)


#Compare and find similar elements of several dif sets
#a = {1,2,3}
#b = {3,4,5}
#c = {3,6,7}
#print(a.intersection(b,c))
##or
#print(a & b & c)


#Find different elements of several sert
#a = {1,2,3}
#b = {3,4,5}
#c = {3,6,7}
#print(a-b-c)
##or
#print(a.difference(b,c))


#Find all different elements of two different sets (simmetric difference)
#In case if it's needed to compare 3 and more sets - we have to create another set to put symmetric difference result in to there and then print it
#a = {1,2,3}
#b = {3,4,5}
#c = {3,6,7}
#print(a^b)
##or
#print(a.symmetric_difference(b))


#to unite several dif. sets we need to use | ot .union
#a = {1,2,3}
#b = {3,4,5}
#c = {3,6,7}
#print(a|b|c)
##or
#print(a.union(b,c))


#name = 'Yurii'
#age = 32
#
#print ('Hello, {}. You are {} years old.'.format(name,age))
##OR
#print(f'Hello {name}. You are {age} years old.')

#my_list = [2024, 3.12]
#some_data = ['Python']
#my_list.extend(some_data)
#my_list.insert(1, 'Python')
#my_list.reverse()
#print (my_list)


##format print wxamples
#name = 'Alice'
#age = 30
#
#message = f'My name is {name}. I am {age/2} years old'
#print(message)
#
#print(f'My name is {name}. I am {age/2} years old')
#
#message = 'Test 2. My name is {}. I am {} years old'.format(name, age)
#print(message)
#
#message = 'Test 3. My name is %s. I am %d years old' % (name, age)
#print(message)
#
#message = 'Test 4. My name is ' + name + '. I am ' + str(age) + ' years old'
#print(message)

#age = 25.6
#print(age, type(age))
#
#age = int(age)
#print(age, type(age))
#
#age = float(age)
#print(age, type(age))

#Приклад програми обчислення точної кількості цілих і дробних частин математичного рівняння на прикладі 
#суми інтернет замовлень
#bill_one = 34.34
#bill_two = 12.01
#bill_three = 17.42
#bill_four = 4.93
#
#final_bill =  bill_one + bill_two + bill_three + bill_four
#
#dollars = int(final_bill)
#cents = int((final_bill - int(final_bill)) * 100)
#'''
#Пояснення формули - в середині дужок одне із значень переводиться у ціле число через що воно втрачає свою
#дробову частину. У результаті ми отримуємо 68.7-68 = 0.7 Далі це число множиться на 100 і його клас 
#змінюється на інт 0.7*100 = 70
#'''
#print(f"Total Price {final_bill}",f"Dollars {dollars}",f"Cents {cents}",sep='\n')

##Перевірка рівності та ідентичності значень
#s1='Hello World!'
#s2='Hello ' + 'World!'
#
#print(s1==s2)
#print(s1 is s2)
#
#print(id(s1))
#print(id(s2))

#Скласти програму визначення номера під'їзду та поверху квартири за заданим номером квартири. 
#У будинку 5 поверхів і 4 квартири на поверсі.
#FLOORS = 5
#APARTMENTS_PER_FLOOR = 4
#
#apartment_number = int(input('Enter apartment number: '))
#apartments_per_entrance = FLOORS * APARTMENTS_PER_FLOOR
#entrance_number = (apartment_number - 1) // apartments_per_entrance + 1
#floor_number = ((apartment_number - 1) % apartments_per_entrance) // APARTMENTS_PER_FLOOR + 1
#print(f"Entrance number {entrance_number}, Floor number {floor_number}")

#print((1-1)//20=1)
#print (((42-1)%20) // 4 +1)

#num1 = int(input('Please enter your number: '))
#if num1 > 0:
#    print(f'Your number {num1} is positive')
#elif num1<0:
#    print(f'Your number {num1} is negative')
#else:
#    print(f'Your number is 0')

#a={}
#b={1,1}
#c=()
#d=[]
#print(type(a))
#print(type(b))
#print(type(c))
#print(type(d))


#x = int(input('Please enter x coordinate: '))
#y = int(input('Please enter y coordinate: '))
#
#point = (x,y)
#
#match point:
#    case (0, 0):
#        print("Точка в центрі координат")  
#    case (0, y):
#        print(f"Точка лежить на осі Y: y={y}")  
#    case (x, 0):
#        print(f"Точка лежить на осі X: x={x}") 
#    case (x, y):
#        print(f"Точка має координати:  x={x}, y={y}") 
#    case _:
#        print("Це не точка")

#l1 = [1,2,3]
#l2=['word1','word2', 'word3','word4']
#for a, b in zip(l1,l2):
#    print(a,b)

#val = '4'
#try:
#    val = int(val)
#except ValueError:
#    print(f"val {val} is not a number")
#else:
#    print(f'entered number: {val} is valid digit?', f'Yes it is {val > 0}', sep='\n')
#finally:
#    print("This will be printed anyway")

#def add_numbers(num1: int, num2: int) -> int:
#    sum = num1 + num2
#    return sum
#
#result = add_numbers(5, 10)
#print(result)  # Виведе: 15

##function for character convertion in to ASCII format and further print where each consicutive pair is printed in new line. 
##pay attention to print constraction since:
##   [f'{key}: {value}' for key, value in my_dict.items()] generates a list of strings, each containing a key-value pair.
##   * unpacks the list so that each string becomes a separate argument to print().
##   sep='\n' specifies that each argument should be separated by a newline character, causing each key-value pair to be printed on a 
##   new line.
#def string_to_codes (string: str) -> dict:
#    codes = {'character':'code'}
#    for q in string:
#        if q not in codes:
#            codes[q] = ord(q)
#    return(codes)
#
#result = string_to_codes('My name is Yurii')
#print (*[f'{key}:{value}' for key, value in result.items()], sep = '\n')




#def factorial(n):
#    print("Виклик функції factorial з n = ", n)
#    if n == 1:
#        print("Базовий випадок, n = 1, повернення 1")
#        return 1
#    else:
#        result = n * factorial(n-1)
#        print("Повернення результату для n = ", n, ": ", result)
#        return result
#
#print(factorial(5))


#try:
#    x = int(input('Please enter your digit: '))
#    if x %2 ==0:
#        print (f'Your digit {x}, is even.')
#    else:
#        print(f'Your digit {x}, is odd')
#except ValueError:
#    print(f'{x} is not a digit! Please enter valid digit: ')

#def discount_price(price, discount):
#    def apply_discount():
#        nonlocal price
#        Price = price*(1-discount)
#    apply_discount()
#
#    
#        
#
#    
#    return price

#def get_fullname (first_name, last_name, middle_name=""):
#    if middle_name :
#        print (f'{first_name} {last_name}')
#    else:
#        print (f'{first_name} {middle_name} {last_name}')
#
#get_fullname('Petro','Zaliznyak')

def format_string(string:str, length:int)->str:
    if len(string)>=length:
        return print(string)
    else:
        return ' ' * (length - len(string) // 2) + string + ' ' * (length - len(string) // 2)

format_string('hello',20)
print(format_string)