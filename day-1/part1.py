import re
from sys import stdin

def get_instructions_input():
    return list(stdin.read().split())

def get_new_number(current_number, text_input):
    number_string = re.search(r"\d+", text_input)
    number = int(number_string.group())  
    if 'L' in text_input:
        new_number = (current_number - number) % 100
    elif 'R' in text_input:
        new_number = (current_number + number) % 100
    return new_number

def get_number_of_zeros(current_number, list_input):
    zero_count = 0
    for element in list_input:
        current_number = get_new_number(current_number, element)
        if current_number == 0:
            zero_count += 1
    return zero_count

if __name__ == "__main__":
    list_input = get_instructions_input()
    current_number = 50
    result = get_number_of_zeros(current_number, list_input)
    print(result)


