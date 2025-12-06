from sys import stdin
import operator

def get_input():
    overall_list = []
    for line in stdin:
        line_list = list(filter(lambda x: x != '\n', list(line)))
        overall_list.append(line_list)
    return overall_list

def get_list_of_columns_from_input(input):
    string_list = []
    for i in range(len(input[0])):
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
    total = 0
    for i in range(len(columns_list)):
        item = columns_list[i]
        if '+' in item or '*' in item:
            operator_function = get_operator(item[-1])
            result = int(item[0:-1])
        elif item.isspace():
            total += result
        else:
            result = operator_function(result, int(item))
    total += result
    return total

if __name__ == "__main__":
    input = get_input()
    columns_list = get_list_of_columns_from_input(input)
    result = get_total_from_columns_list(columns_list)
    print(result)