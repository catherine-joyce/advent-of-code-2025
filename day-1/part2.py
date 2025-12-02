import re
from sys import stdin

def create_numbers_list():
    numbers = []
    for i in range(0, 100):
        numbers.append(i)
    return numbers


def get_new_number_part_2(numbers, current_number, text_input):
    zero_count = 0
    number_string = re.search(r"\d+", text_input)
    number = int(number_string.group())
    if 'L' in text_input:
        index = (current_number - number) % 100
        if current_number != 0 and (current_number - (number % 100)) < 0:
            zero_count = 1
    elif 'R' in text_input:
        index = (current_number + number) % 100
        if current_number != 0 and (current_number + (number % 100)) > 100:
            zero_count = 1
    zero_count += (number // 100)
    return numbers[index], zero_count

def get_instructions_input():
    return list(stdin.read().split())
 

def get_number_of_zeros_part_2(numbers, current_number, list_input):
    zero_count = 0
    for element in list_input:
        current_number, zero_number = get_new_number_part_2(numbers, current_number, element)
        zero_count += zero_number
        if current_number == 0:
            zero_count = zero_count + 1
    return zero_count


if __name__ == "__main__":
    list_input = get_instructions_input()
    current_number = 50
    numbers = create_numbers_list()
    result = get_number_of_zeros_part_2(numbers, current_number, list_input)
    print(result)


