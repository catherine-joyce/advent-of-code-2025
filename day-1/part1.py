import re
from sys import stdin

def create_numbers_list():
    numbers = []
    for i in range(0, 100):
        numbers.append(i)
    return numbers


def get_new_number(numbers, current_number, text_input):
    if 'L' in text_input:
        number_string = re.search(r"\d+", text_input)
        number = int(number_string.group())
        index = (current_number - number) % 100
        new_number = numbers[index] 
        return new_number
    elif 'R' in text_input:
        number_string = re.search(r"\d+", text_input)
        number = int(number_string.group())
        index = (number + current_number) % 100
        new_number = numbers[index] 
        return new_number

def get_instructions_input():
    return list(stdin.read().split())
 

def get_number_of_zeros(numbers, current_number, list_input):
    zero_count = 0
    for element in list_input:
        current_number = get_new_number(numbers, current_number, element)
        if current_number == 0:
            zero_count += 1
    return zero_count


if __name__ == "__main__":
    list_input = get_instructions_input()
    current_number = 50
    numbers = create_numbers_list()
    result = get_number_of_zeros(numbers, current_number, list_input)
    print(result)


