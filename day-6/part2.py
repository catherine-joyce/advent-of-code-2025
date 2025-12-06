from sys import stdin
import operator

def get_instructions_input():
    overall_list = []
    for line in stdin:
        line_list = list(filter(lambda x: x != '\n', list(line)))
        overall_list.append(line_list)
    return overall_list

def get_list_of_columns_from_input(input):
    string_list = []
    for i in range(len(input[0])-1 , -1, -1):
        total_string = ""
        for j in range(len(input)):
            total_string = total_string + input[j][i]
        string_list.append(total_string)
    return string_list

def get_operator(operator_string):
    if operator_string == '*':
        return operator.mul
    elif operator_string == '+':
        return operator.add
    
def get_total_from_columns_list(columns_list):
    i = 0
    numbers_list = []
    total = 0
    while i <= len(columns_list):
            item = columns_list[i]
            if '+' in item or '*' in item:
                numbers_list.append(int(item[0:-1]))
                operator_function = get_operator(item[-1])
                result = numbers_list[0]
                for x in range(1, len(numbers_list)):
                   result = operator_function(result, numbers_list[x])
                total += result
                numbers_list = []
                i += 2
            else:
                numbers_list.append(int(item))
                i += 1
    return total

if __name__ == "__main__":
    input = get_instructions_input()
    columns_list = get_list_of_columns_from_input(input)
    result = get_total_from_columns_list(columns_list)
    print(result)