# import sys
from pathlib import Path
# from colorama import Fore, Style
from processing import display_directory_structure

str_path = input('Please enter directory: ')

def directory_structure(dir):
    if Path.is_file(dir):
        print(f"Error: '{dir}' is a file")
    elif not Path.exists(dir):
        print(f"Error: '{dir}' is not a valid directory.")
    else:
        display_directory_structure(dir)
        # print(f"'{dir}' is a valid directory.")
        

dir = Path(str_path)
# dir = '/Users/yuriyodynets/Desktop/Projects/My_repo/First_repo/HomeWork'
directory_structure(dir)