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


name = 'Yurii'
age = 32

print ('Hello, {}. You are {} years old.'.format(name,age))
#OR
print(f'Hello {name}. You are {age} years old.')