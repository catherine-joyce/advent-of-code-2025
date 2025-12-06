from part2 import get_list_of_columns_from_input, get_total_from_columns_list

input = [
    ['1', '2', '3', ' ', '3', '2', '8', ' ', ' ', '5', '1', ' ', '6', '4', ' '], 
    [' ', '4', '5', ' ', '6', '4', ' ', ' ', '3', '8', '7', ' ', '2', '3', ' '], 
    [' ', ' ', '6', ' ', '9', '8', ' ', ' ', '2', '1', '5', ' ', '3', '1', '4'], 
    ['*', ' ', ' ', ' ', '+', ' ', ' ', ' ', '*', ' ', ' ', ' ', '+', ' ', ' ']
    ]

def test_calculate_total():
    columns_list = get_list_of_columns_from_input(input)
    result = get_total_from_columns_list(columns_list)
    assert result == 3263827