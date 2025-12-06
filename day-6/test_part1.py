import operator

from part1 import get_operator, calculate_column, get_total_all_columns

def test_get_operator_multiply():
    input = [['123', '328', '51', '64'], ['45', '64', '387', '23'], ['6', '98', '215', '314'], ['*', '+', '*', '+']]
    operator_string = input[-1][0]
    print(operator_string)
    result = get_operator(operator_string)
    assert result == operator.mul

def test_get_operator_add():
    input = [['123', '328', '51', '64'], ['45', '64', '387', '23'], ['6', '98', '215', '314'], ['*', '+', '*', '+']]
    operator_string = input[-1][1]
    print(operator_string)
    result = get_operator(operator_string)
    assert result == operator.add

def test_calculate_first_column():
    input = [['123', '328', '51', '64'], ['45', '64', '387', '23'], ['6', '98', '215', '314'], ['*', '+', '*', '+']]
    result = calculate_column(input, 0)
    assert result == 33210
    
def test_calculate_second_column():
    input = [['123', '328', '51', '64'], ['45', '64', '387', '23'], ['6', '98', '215', '314'], ['*', '+', '*', '+']]
    result = calculate_column(input, 1)
    assert result == 490
    
def test_calculate_third_column():
    input = [['123', '328', '51', '64'], ['45', '64', '387', '23'], ['6', '98', '215', '314'], ['*', '+', '*', '+']]
    result = calculate_column(input, 2)
    assert result == 4243455
    
def test_calculate_fourth_column():
    input = [['123', '328', '51', '64'], ['45', '64', '387', '23'], ['6', '98', '215', '314'], ['*', '+', '*', '+']]
    result = calculate_column(input, 3)
    assert result == 401

def test_get_total():
    input = [['123', '328', '51', '64'], ['45', '64', '387', '23'], ['6', '98', '215', '314'], ['*', '+', '*', '+']]
    result = get_total_all_columns(input)
    assert result == 4277556