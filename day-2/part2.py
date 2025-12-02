import re
from sys import stdin

def get_input():
    return list(stdin.read().split(','))

def get_factors_list_for_number(number):
    factors = []
    for i in range(1,number+1):
        if number % i == 0 and number != i:
            factors.append(i)
    return factors

def get_number_of_invalid_ids_part_2(id_range):
    id_list = re.findall(r"\d+", id_range)
    invalid_list = []
    for i in range(int(id_list[0]), int(id_list[1])+1):
        element = str(i)
        factors_list = get_factors_list_for_number(len(element))
        for factor in factors_list:
            digits = ""
            for x in range(0, factor):
               digits += element[x]
            if (digits * ((len(element)) // int(factor))) == element:
               invalid_list.append(int(element)) 
               break
    return len(invalid_list), invalid_list

def sum_of_invalid_ids(input_list):
    total_invalid_id_list = []
    for item in input_list:
        number, invalid_list = get_number_of_invalid_ids_part_2(item)
        total_invalid_id_list.extend(invalid_list)
        total = 0
        for item in total_invalid_id_list:
            total += item
    return total

if __name__ == "__main__":
    list_input = get_input()
    result = sum_of_invalid_ids(list_input)
    print(result)

