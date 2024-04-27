import math
from log import log_error, log_info, log_warning

def calculate_square_root(numbers:list) -> None:
    for number in numbers:
        try:
            if number <0:
                log_warning(f'Negative digit found: {number}. Skipping.')
                continue
            root=math.sqrt(number)
            log_info(f'Square root from digit {number} - {root:.2f}')
            
        except Exception as e:
            log_error(f'Error during root calculation for {number}:{e}')

if __name__=='__main__':
    numbers = [16, -4, 9, 25, 0, 4, "16"]
    calculate_square_root(numbers)