import re
from sys import stdin

def get_input():
    return list(stdin.read().split(','))

def get_number_of_invalid_ids(id_range):
    id_list = re.findall(r"\d+", id_range)
    number = 0
    invalid_list = []
    for i in range(int(id_list[0]), int(id_list[1])+1):
        digits = ""
        element = str(i)
        if len(element) % 2 == 0:
            for x in range(0, len(element) // 2):
               digits += element[x]
            if (digits + digits) == element:
               number += 1
               invalid_list.append(int(element)) 
    return number, invalid_list

def sum_of_invalid_ids(input_list):
    total_invalid_id_list = []
    for item in input_list:
        number, invalid_list = get_number_of_invalid_ids(item)
        total_invalid_id_list.extend(invalid_list)
        total = 0
        for item in total_invalid_id_list:
            total += item
    return total


if __name__ == "__main__":
    list_input = get_input()
    result = sum_of_invalid_ids(list_input)
    print(result)
