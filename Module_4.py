#from pathlib import Path
#import sys
#file_name = Path('./arg.py')
#
#file_name.unlink(missing_ok=True)

#try:
#    file = open(file_name/'jokes.txt', 'r', encoding='utf-8')
#    try:
#        while True:
#            line=file.readline()
#            if not line:
#                break
#            print(line, end='')
#    except OSError:
#        print('Error while reading "file"')
#    finally:
#        file.close()
#except OSError:
#    print('Error while opening "file"')
#   
# --------OR---------
#try:
#    with open (file_name/'jokes.txt', 'r+', encoding='utf-8') as file:
#        for line in file:
#            print(line, end='')
#
#except Exception as e:
#    print (f'{e}while file')

##видалення папки за вказаним шляхом
#try:
#    Path.rmdir(file_name)
#    print(f'{file_name} directory has been removed')
#except FileNotFoundError as e:
#    print(f'{file_name} directory could not be found')

contacts={'a':'1','b':'2'}

def show_all(contacts):
    for name, phone in contacts.items():
        print(f'{name}: {phone}')
show_all(contacts)