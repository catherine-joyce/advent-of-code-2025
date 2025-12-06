from sys import stdin
import operator

def get_instructions_input():
    overall_list = []
    for line in stdin:
        line_list = list(filter(lambda x: x != '\n', list(line)))
        overall_list.append(line_list)
    return overall_list

def get_operator(operator_string):
    if operator_string == '*':
        return operator.mul
    elif operator_string == '+':
        return operator.add

def calculate_column(input, column_number):
    result = int(input[0][column_number])
    for i in range(1, len(input) - 1):
        operator_function = get_operator(input[-1][column_number])
        result = operator_function(result, int(input[i][column_number]))
    return result

def get_total_all_columns(input):
    total = 0
    for i in range(len(input[0])):
        total += calculate_column(input, i)
    return total


if __name__ == "__main__":
    input = get_instructions_input()
    print(input)

# overall_list.append(list(line))

[['1', '2', '3', ' ', '3', '2', '8', ' ', ' ', '5', '1', ' ', '6', '4', ' '], 
 [' ', '4', '5', ' ', '6', '4', ' ', ' ', '3', '8', '7', ' ', '2', '3', ' '], 
 [' ', ' ', '6', ' ', '9', '8', ' ', ' ', '2', '1', '5', ' ', '3', '1', '4'], 
 ['*', ' ', ' ', ' ', '+', ' ', ' ', ' ', '*', ' ', ' ', ' ', '+', ' ', ' ']]