import os
from colorama import Fore, Style

def display_directory_structure(directory):
    for root, dirs, files in os.walk(directory):
        # Відображення шляху поточної директорії
        print(Style.BRIGHT + Fore.BLUE + root + Style.RESET_ALL)

        # Відображення піддиректорій
        for dir_name in dirs:
            print(Fore.CYAN + f"  {dir_name}/" + Style.RESET_ALL)

        # Відображення файлів
        for file_name in files:
            print(Fore.WHITE + f"  {file_name}" + Style.RESET_ALL)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    display_directory_structure(directory_path)